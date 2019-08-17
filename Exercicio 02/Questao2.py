import psycopg2
try:

  # Conecta no database
  connection = psycopg2.connect(user = "postgres",
                                  password = "4560",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "pg_db")
  cursor = connection.cursor()
    
  
  # Cria a tabela com nome idade e telefone
  cursor.execute("CREATE TABLE pessoa (id_pessoa int, nm_pessoa varchar(50), ds_pessoa varchar(50), nr_idade int, PRIMARY KEY(id_pessoa));")
  
  # Popular a tabela
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (1, 'Simão', 'Chamado Pedro, o chefe do grupo', 30);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (2, 'André', 'Irmão de Pedro', 33);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (3, 'Tiago', 'Filho de Zebedeu', 30);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (4, 'João', 'Irmão de Tiado', 24);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (5, 'Felipe', '-', 30);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (6, 'Bartolomeu', 'Considerado como Natanael', 25);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (7, 'Tomé', 'O incrédulo', 29);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (8, 'Mateus', 'O publicano', 31);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (9, 'Tiago', 'Filho de Alfeu', 26);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (10, 'Tadeu', '-', 26);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (11, 'Simão Cananeu', 'O zelote', 28);")
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (12, 'Judas Iscariotes', 'Aquele que o traiu e foi substituído por Matias', 30);")

  # Prevenção de SqlInjection
  possible_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z', 
  						'á', 'ã', 'à', 'â', 'í', 'ì', 'î', 'ú', 'ù', 'û', 'é', 'è', 'ê', 'ó', 'ò', 'õ', 'ô']
  name = input('Digite o nome: ')

  for letter in name.lower():
  	if letter not in possible_characters:
  		raise Exception("Caractere \'" + letter + "\' não permitido")
  		
  cursor.execute("SELECT * FROM pessoa WHERE nm_pessoa = %s;", (name,)) 
  
  for row in cursor.fetchall():
    print (row)

except (Exception) as error :
    print ("Error:", error)

finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL: conexão fechada com sucesso.")

