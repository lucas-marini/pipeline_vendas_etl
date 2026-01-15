import pandas as pd

def transform(df):
    #padronizar data
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    #remover registros sem quantidade ou preço
    df = df.dropna(subset=['quantidade','preco_unitario'])
    #cria coluna de valor total
    df['valor_total'] = df['quantidade'] * df['preco_unitario']

    return df
