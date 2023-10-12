import mysql.connector
import logging
#FORMAT = '%(asctime)s;%(message)s'
#logging.basicConfig(Level=logging.NOTSET, format = FORMAT)


print(logging.info("Connexion à la BDD"))
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  port = "3306",
  password="dQZ5]A;S7%=8@xnpNvhD?J",
  database="dwh_sdp_ventes"
)
print(logging.info("connexion établie"))

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("DROP TABLE DWH_D_E_COMMERCE_CLIENT")

mycursor.execute("""CREATE TABLE IF NOT EXISTS DWH_D_E_COMMERCE_CLIENT (ID_CLIENT INT PRIMARY KEY, DATE_INSCRIPTION DATETIME,  NOM VARCHAR(255), PRENOM VARCHAR(255), E_MAIL VARCHAR(255), ADRESSE VARCHAR(255), CODE_POSTALE VARCHAR(255), VILLE VARCHAR(255), TEL_FIXE VARCHAR(32), TEL_MOBILE VARCHAR(32), 
                 NOM_ENTREPRISE VARCHAR(255),  MESSAGE mediumtext, MOTEUR_RECHERCHE VARCHAR(255));""")

mycursor.execute("""INSERT INTO DWH_D_E_COMMERCE_CLIENT(ID_CLIENT, DATE_INSCRIPTION,  NOM, PRENOM, E_MAIL, ADRESSE, CODE_POSTALE, VILLE, TEL_FIXE, TEL_MOBILE, NOM_ENTREPRISE,  MESSAGE, MOTEUR_RECHERCHE)
                 SELECT c.id_customer id_client,  c.date_add DATE_INSCRIPTION,  c.lastname NOM, c.firstname PRENOM, c.email E_MAIL, a.address1 ADRESSE, a.postcode CODE_POSTALE, 
a.city VILLE, a.phone TEL_FIXE, a.phone_mobile TEL_MOBILE, a.company NOM_ENTREPRISE, m.message MESSAGE, m.user_agent MOTEUR_RECHERCHE
from ope.ps_customer c
INNER JOIN ope.ps_address a ON a.id_address = c.id_customer
INNER JOIN ope.ps_customer_message m on m.id_customer_message = c.id_customer
Group by c.id_customer;""")