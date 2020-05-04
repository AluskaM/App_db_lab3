import csv
import cx_Oracle
username = 'bd'
password = 'makarenko'
database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

csv_file = open('Google-Playstore-32K.csv', encoding='utf-8', errors='ignore')
reader = csv.reader(csv_file, delimiter=',')

category_unique = []
audience_unique = []

tables = ['Category', 'Audience', 'App', 'Reviews']
for table in tables:
    cursor.execute("DELETE FROM " + table)
i=1
try:
    for row in reader:
        app_name = row[0]
        category_name = row[1]
        reviews_count = row[3]
        price = row[6]
        audience_type = row[7]

        if category not in category_unique:
                category_unique.append(category)
                query = '''INSERT INTO Description(category) VALUES(:category)'''
                cursor.execute(query, category=category)

        if audience not in audience_unique:
            audience_unique.append(audience)
            query = '''INSERT INTO Description(audience) VALUES(:audience)'''
            cursor.execute(query, audience=audience)

        query = '''
               INSERT INTO App(app_name, category_name, audience_type, price) 
                   VALUES(:app_name, :category_name, :audience_type, :price)'''
        cursor.execute(query, app_name=app_name, category_name=category_name, audience_type=audience_type, price=price)

        query = '''
                     INSERT INTO Reviews(reviews_count, app_name, review_date) 
                         VALUES(:reviews_count, :app_name, :review_date)'''
        cursor.execute(query, reviews_count=reviews_count, app_name=app_name, review_date='05.05.2017')

    i+=1


connection.commit()
cursor.close()
connection.close()
csv_file.close()

















