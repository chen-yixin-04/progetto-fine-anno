# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS FAST_FOOD")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS FAST_FOOD_Unit (
    restaurant VARCHAR(30) NOT NULL,
    item INTEGER,
    calories INTEGER,
    cal_fat INTEGER,
    total_fat INTEGER,
    sat_fat INTEGER,
    trans_fat,
    cholesterol INTEGER,
    sodium INTEGER,
    total_carb INTEGER,
    PRIMARY KEY (Unit)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM FAST_FOOD_Unit")
mydb.commit()

#Read data from a csv file
fastfood_data = pd.read_csv('./fastfood.csv', index_col=False, delimiter = ',')
fastfood_data = fastfood_data.fillna('Null')
print(fastfood_data.head(20))

#Fill the table
for i,row in fastfood_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO FAST_FOOD_Unit VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM FAST_FOOD_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)