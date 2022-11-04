import requests
import json
import mysql.connector

try:
    mydb = mysql.connector.connect(host = 'localhost', user = 'root',password = '',database='populationdb')
except mysql.connector.Error as e:
    print("Connector error ",e)


mycursor = mydb.cursor()

data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text


data_info = json.loads(data)

for i in data_info["data"]:
    year = str(i["ID Year"])
    population = str(i['Population'])
    sql = "INSERT INTO `population`(`id_nation`, `nation`, `id_year`, `population`, `slug_nation`) VALUES ('"+i['ID Nation']+"','"+i['Nation']+"','"+year+"','"+population+"','"+i['Slug Nation']+"')"

    mycursor.execute(sql)

    mydb.commit()

    print('Inserted the value succesfully')