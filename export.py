import csv
import cx_Oracle
username = 'bd'
password = 'makarenko'
database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

csv_file = open('Google-Playstore-32K.csv', 'w', newline='')


tables = ['Category', 'Audience', 'App', 'Reviews']


try:
    for table in tables:
       with open(table + '.csv', 'w', newline = '') as csvfile:
       cursor.execute('SELECT * FROM ' + table)
       cursor.execute(query)
       row = cursor.fetchone()
                 
       csv_writer = csv.writer(csv_file, delimiter=',')
       csv_writer.writerow(['Category', 'Audience', 'App', 'Reviews'])
        for data in row:
            csv_writer.writerow(data)

cursor.close()
connection.close()
csv_file.close()
