import requests
from django.core.exceptions import ValidationError

def validar_cnpj_api(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    if response.status_code != 200:
        raise ValidationError('Erro ao consultar CNPJ na Receita.')
    dados = response.json()
    if 'status' in dados and dados['status'] == 'ERROR':
        raise ValidationError(f'CNPJ inválido: {dados.get("message", "Erro desconhecido.")}')
    if dados.get('situacao') != 'ATIVA':
        raise ValidationError(f'CNPJ inativo: {dados.get("situacao")}')
    return dados
