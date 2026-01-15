import pyodbc

def load(df):
    conn = pyodbc.connect(
        "driver={odbc driver 17 for sql server};"
        "server=DESKTOP-SSF2SBK;"
        "database=vendasDW;"
        "Trusted_connection=yes;"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
                       insert into fato_vendas
                       values (?,?,?,?,?,?,?,?)
        """,
        row.id_venda,
        row.data_venda,
        row.produto,
        row.categoria,
        row.quantidade,
        row.preco_unitario,
        row.valor_total,
        row.vendedor)

    conn.commit()
    conn.close()
