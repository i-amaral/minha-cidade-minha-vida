"""Get data for Brazilian municipalities from IBGE API"""

from api_ibge import get_data

URL = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'

df_municipios = get_data(URL) \
    .rename(
        columns={
            # Municipio
            'id': 'ID_MUNICIPIO',
            'nome': 'NOME_MUNICIPIO',
            # Microrregiao
            'microrregiao.id': 'ID_MICRORREGIAO',
            'microrregiao.nome': 'NOME_MICRORREGIAO',
            # Regiao Immediata
            'regiao-imediata.id': 'ID_REGIAO_IMEDIATA',
            'regiao-imediata.nome': 'NOME_REGIAO_IMEDIATA',
            # Regiao Intermediaria
            'regiao-imediata.regiao-intermediaria.id': 'ID_REGIAO_INTERMEDIARIA',
            'regiao-imediata.regiao-intermediaria.nome': 'NOME_REGIAO_INTERMEDIARIA',
            # UF
            'regiao-imediata.regiao-intermediaria.UF.id': 'ID_UF',
            'regiao-imediata.regiao-intermediaria.UF.sigla': 'SIGLA_UF',
            'regiao-imediata.regiao-intermediaria.UF.nome': 'NOME_UF',
            'regiao-imediata.regiao-intermediaria.UF.regiao.id': 'ID_REGIAO_UF',
            'regiao-imediata.regiao-intermediaria.UF.regiao.sigla': 'SIGLA_REGIAO_UF',
            'regiao-imediata.regiao-intermediaria.UF.regiao.nome': 'NOME_REGIAO_UF'
            }
        )

df_municipios = df_municipios[[
    'ID_MUNICIPIO',
    'NOME_MUNICIPIO',
    'ID_MICRORREGIAO',
    'NOME_MICRORREGIAO',
    'ID_REGIAO_IMEDIATA',
    'NOME_REGIAO_IMEDIATA',
    'ID_REGIAO_INTERMEDIARIA',
    'NOME_REGIAO_INTERMEDIARIA',
    'ID_UF',
    'SIGLA_UF',
    'NOME_UF',
    'ID_REGIAO_UF',
    'SIGLA_REGIAO_UF',
    'NOME_REGIAO_UF'
    ]]

cols_texto = df_municipios.select_dtypes(include=['object', 'string']).columns

df_municipios[cols_texto] = df_municipios[cols_texto].apply(lambda col: col.str.upper())

df_municipios.to_excel('df_municipios.xlsx', index=False)
