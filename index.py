import pdb
import random
import psycopg2

#Select
def selectUser():
	conn = psycopg2.connect("dbname=testpython user=postgres host=localhost password=1234")
	cur = conn.cursor()
	cur.execute("SELECT * FROM testuser;")

	res=cur.fetchall()
	if len(res)==0:
		print("Aucun utilisateur enregistré")
	else:
		print(res)

#Insert
def insertUser():
	rndValue=random.randint(900,290948999)
	name="John"+str(rndValue)
	sirname="Doe"+str(rndValue)

	conn = psycopg2.connect("dbname=testpython user=postgres host=localhost password=1234")
	cur = conn.cursor()
	cur.execute("INSERT INTO testuser (name, sirname) VALUES (%s, %s)",(str(name),str(sirname)))
	conn.commit()
	cur.close()
	conn.close()

#Create
def initDB():
	conn = psycopg2.connect("dbname=testpython user=postgres host=localhost password=1234")
	cur = conn.cursor()
	try:
		cur.execute("CREATE TABLE testuser (id serial PRIMARY KEY, name varchar, sirname varchar);")
	except psycopg2.errors.lookup("42P07"):
		print("Base de données déjà initialisée")
		insertUser()
		selectUser()
	
	cur.close()
	conn.commit()
	conn.close()

#Appel de fonction
initDB()

