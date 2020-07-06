import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd
import sqlite3
from sqlite3 import Error


df = pd.read_csv("bi_val.csv") 
print(df)
db_file = r"C:\Users\saseendr\Desktop\DBE_chatbot\pythonsqlite.db"

page = requests.get('https://confluence.in.here.com/display/EV/EarthCore+Validations+Guide')

soup = BeautifulSoup(page.text, 'html.parser')
li = [a['href'] for a in soup.find_all('a', href=True) if a.text]
matching = [s for s in li if "EV/EC." in s]
xyz = []
i=0
for x in matching:
    x = x[:8] + '/public' + x[8:]
    xyz.insert(i,x)
    i = i+1
for i in range(len(xyz)):
    if xyz[i] =='/display/public/EV/EC.BLDG001' or xyz[i] =='/display/public/EV/EC.ROAD001':
        pass
    else:
        url = requests.get('https://confluence.in.here.com' + xyz[i])
        
        bsoup = BeautifulSoup(url.text, 'html.parser')
        for row in bsoup.select('tbody tr'):
            row_text = [x.text for x in row.find_all('td')] 
            if 'Rule Code' in row_text:
                print(row_text[1], row_text[1],xyz[i],xyz[i],xyz[i])
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """INSERT INTO rule_codes (rule_name, rule_code, rule_description, severity, link) 
                                           VALUES 
                                           (? , ?, ?, ?, ?) """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1], row_text[1],xyz[i],xyz[i],xyz[i]))
                    
                    connection.commit()
                    print(cursor.rowcount, "Record inserted successfully into Laptop table")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                
            elif 'Rule Name' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET rule_name = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table1")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                
            
            elif 'Rule Description' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET rule_description = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table2")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
            
            
            elif 'Severity' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET severity = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table3")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                
                
            elif 'Error Type' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET error_type = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table3")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
            
            elif 'LE Allowed' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET le_allowed = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table3")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                    
            elif 'Document Owner' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET document_owner = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table3")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                    
                     
            elif 'JIRA Issues' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET jira_issues = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table3")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                    
            elif 'Document status' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET document_status = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table4")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
            
            
            
            elif 'Product' in row_text:
                try:
                    connection  = sqlite3.connect(db_file)
                    mySql_insert_query = """UPDATE rule_codes SET product = ? 
                                           
                                           WHERE link =  ? """

                    cursor = connection.cursor()
                    cursor.execute(mySql_insert_query,(row_text[1],xyz[i]))
                    connection.commit()
                    print(cursor.rowcount, "Record updated successfully into Laptop table4")
                    cursor.close()

                except Error as error:
                    print("Failed to insert record into Laptop table {}".format(error))
                break
                