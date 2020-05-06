
import csv
import cx_Oracle
username = 'bd'
password = 'makarenko'
database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

csv_file = open('Google-Playstore-32K.csv', encoding='utf8', errors='ignore')
reader = csv.reader(csv_file, delimiter=',')
next(reader, None)


category_unique = []
audience_unique = []

tables = ['App', 'Category', 'Audience', 'Reviews']
for table in tables:
    cursor.execute("DELETE FROM " + table)
row_num = 0
i=1
try:
    for row in reader:
        app_name = row[0]
        category_name = row[1]
        reviews_count = row[3]
        price = row[6]
        new_price = str(price)
        audience_type = row[7]

        if category_name not in category_unique:
                category_unique.append(category_name)
                query = '''INSERT INTO Category(category_name) VALUES(:category_name)'''
                cursor.execute(query, category_name=category_name)

        if audience_type not in audience_unique:
            audience_unique.append(audience_type)
            query = '''INSERT INTO Audience(audience_type) VALUES(:audience_type)'''
            cursor.execute(query, audience_type=audience_type)
    
        if reviews_count == '':
            reviews_count = 0
        query = '''
                     INSERT INTO Reviews(id,reviews_count, app_name) 
                         VALUES(:id, :reviews_count, :app_name)'''
        cursor.execute(query,id=i, reviews_count=reviews_count, app_name=app_name)

        if new_price[0] == '$':
            f_price = float(new_price[1:])
        else:
            f_price = 0
                        
                query = ''' INSERT INTO App(id, app_name, category_name, audience_type, price) 
                   VALUES(:id, :app_name, :category_name, :audience_type, :price)'''
        cursor.execute(query,id=i, app_name=app_name, category_name=category_name, audience_type=audience_type, price=f_price)
        row_num += 1
i+=1
    

except:
    print('Error')
    raise

finally:
    connection.commit()
    cursor.close()
    connection.close()
    csv_file.close()

