import pymysql
# Creation classe du connection au base de donne
class Database:
    def __init__(self): 
        try:
            self.connection = pymysql.connect(
                host= 'localhost',
                user = 'root',
                password='',
                database= 'test'
            )
            connexion="Connexion"
            print(connexion)
            self.cursor =self.connection.cursor()

        except Exception as e:
            erreur = "erreur"
            print(erreur)
            return erreur, f"echec de la connexion: {e}"

    def insert_data(self, data):
        try:
            self.cursor.execute("INSERT INTO test(name,email, password) VALUES (%s,%s, %s)", data)
            self.connection.commit()
            print("Insertion reussite")
            return  "Insertion reussite"
        except Exception as e:
            self.connection.rollback()
            print("erreur:", e)

    # Fonction de connexion avec le donne du base de donne

    def FormLogin(self, email, password_hash):
        try:
            self.cursor.execute("SELECT * FROM `test` WHERE email=%s", (email))
            user=self.cursor.fetchone()

            if user is None:
                return False
            if user[3]!=password_hash:
                return False
            else:
                return True,
        except Exception as e:
            self.connection.rollback()
            print("erreur:", e)
            return False
        