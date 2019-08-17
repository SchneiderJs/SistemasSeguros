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
  cursor.execute("INSERT INTO pessoa (id_pessoa, nm_pessoa, ds_pessoa, nr_idade) VALUES (1, 'Simão', 'O chefe do grupo', 30);")


  platform = input('Enter language: ')
  cursor.execute("SELECT * FROM platforms WHERE language = '%s';" % platform)
  
  for row in cursor.fetchall():
    print (row)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

