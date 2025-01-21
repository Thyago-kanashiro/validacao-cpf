import logging
import azure.functions as func
import json

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica dígitos repetidos (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    # Verifica se os dígitos calculados são iguais aos informados
    return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Requisição recebida para validação de CPF.')
    
    cpf = req.params.get('cpf')
    if not cpf:
        return func.HttpResponse(
            "Por favor, informe um CPF no parâmetro 'cpf'.",
            status_code=400
        )
    
    valido = validar_cpf(cpf)
    resposta = {
        "cpf": cpf,
        "valido": valido
    }
    
    return func.HttpResponse(json.dumps(resposta), mimetype="application/json")