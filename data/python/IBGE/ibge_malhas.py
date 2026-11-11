"""Test code"""

from api_ibge import get_data

URL = 'https://servicodados.ibge.gov.br/api/v4/malhas/municipios/3304557/metadados'

df = get_data(URL)

print(df)
