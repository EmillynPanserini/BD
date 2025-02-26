import psycopg2
from itertools import combinations

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="DataCombinacao'",    
    user="postgres",           
    password="l25e04ca",          
    host="localhost",          # Ou o endereço do servidor PostgreSQL
    port="5432"             
)
cursor = conn.cursor()

# Criar tabela de transações
cursor.execute('''
CREATE TABLE IF NOT EXISTS transacoes (
    id SERIAL PRIMARY KEY,
    leite BOOLEAN,
    cafe BOOLEAN,
    cerveja BOOLEAN,
    pao BOOLEAN,
    manteiga BOOLEAN,
    arroz BOOLEAN,
    feijao BOOLEAN
)
''')

# Dados da tabela
transacoes = [
    (False, True,  False, True,  True,  False, False),
    (True,  False, True,  True,  True,  False, False),
    (False, True,  False, True,  True,  False, False),
    (True,  True,  False, True,  True,  False, False),
    (False, False, True,  False, False, False, False),
    (False, False, False, False, True,  False, True ),
    (False, False, False, True,  True,  False, False),
    (False, False, False, False, True,  True,  False),
    (True,  False, False, False, False, True,  False),
    (False, False, False, False, False, True,  False)
]

# Inserir transações no banco de dados
cursor.executemany('''
INSERT INTO transacoes (leite, cafe, cerveja, pao, manteiga, arroz, feijao)
VALUES (%s, %s, %s, %s, %s, %s, %s)
''', transacoes)

conn.commit()  # Salvar as mudanças

# Nomes dos itens (colunas da tabela)
itens = ['leite', 'cafe', 'cerveja', 'pao', 'manteiga', 'arroz', 'feijao']

# Função para calcular suporte
def calcular_suporte(cursor, itemset):
    query = f'''
    SELECT COUNT(*) FROM transacoes
    WHERE {' AND '.join([f"{item} = TRUE" for item in itemset])}
    '''
    cursor.execute
