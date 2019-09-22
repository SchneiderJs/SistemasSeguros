import psycopg2
try:

  # Cria uma conexão com o banco de dados
  connection = psycopg2.connect(user = "postgres",
                                password = "4560",
                                host="localhost",
                                port = "5432",
                                database = "pg_db")
  cursor = connection.cursor()

  # Cria a tabela professor com os campos nome, titulação e departamento
  cursor.execute("CREATE TABLE professor (id_professor int, nm_professor varchar(50), ds_titulacao varchar(30), ds_departamento varchar(30), PRIMARY KEY(id_professor));")
  
  # Popula a tabela
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (1, 'Gilvan Justino', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (2, 'Aurélio Faustino Hoppe', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (3, 'Georges Cherry Rodrigues', 'Mestrado', 'Matemática');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (4, 'Luciana Pereira de Araújo Kohler', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (5, 'Everaldo Artur Grahl', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (6, 'Francisco Adell Péricas', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (7, 'Andreza Sartori', 'Doutorado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (8, 'Dalton Solano dos Reis', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (9, 'Marcel Hugo', 'Mestrado', 'Sistemas e Computação');")
  cursor.execute("INSERT INTO professor (id_professor, nm_professor, ds_titulacao, ds_departamento) VALUES (10, 'Joyce Martins', 'Mestrado', 'Sistemas e Computação');")

  # Sql Injection
  name = input('Digite o nome do professor: ')
  cursor.execute("SELECT * FROM professor WHERE nm_professor = '%s';" % name)
  
  # Recupera e mostra os registros
  print('Registro(s): ', cursor.rowcount)
  for row in cursor.fetchall():
    print (row)

except (Exception, psycopg2.Error) as error:
  print ("Erro ao conectar.", error)

finally:
# Fecha a conexão
  if (connection):
    cursor.close()
    connection.close()