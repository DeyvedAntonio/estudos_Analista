import pandas as pd
import sqlite3

# Leia o arquivo CSV usando o Pandas
df = pd.read_csv('netflix_titles.csv')

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('desafio_descomplidados.db')

# Salve o DataFrame no banco de dados SQLite
df.to_sql('netflix_title', conn, index=False, if_exists='replace')

# Feche a conexão
conn.close()
