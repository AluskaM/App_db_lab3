import cx_Oracle
username = 'bd'
password = 'makarenko'
database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

print('1.Вивести кількість платних додатків по кожній категорії. \n')
query1 = '''
SELECT category_name, COUNT(app_name) app_count
FROM Apps
WHERE price!=0
GROUP BY category_name
ORDER BY  app_count,category_name
'''
cursor.execute(query1)
for row in cursor:
    print(row)



print("\n2.Вивести відстоткове відношення додатків по аудиторії людей.\n")
query2 = """
SELECT audience_name , round((COUNT(app_name))/ (SELECT COUNT(*) FROM App)*100, 2)  persent                                                                                                             
FROM Apps
GROUP BY audience_name
ORDER BY persent DESC, audience_name;
"""
cursor.execute(query2)
for row in cursor:
    print(row)



print("\n3.Вивести динаміку залежності кількості відгуків додатків від їх ціни, які передбачені для всіх груп користувачів. \n")
query3 = """
SELECT price, SUM(reviews) sum_reviews
FROM Apps
WHERE audience_name='Everyone'
GROUP BY price
ORDER BY price;
"""
cursor.execute(query3)
for row in cursor:
    print(row)

cursor.close()
connection.close()
