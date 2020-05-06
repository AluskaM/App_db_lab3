

import cx_Oracle
import chart_studio
import re
chart_studio.tools.set_credentials_file(username='AllaM', api_key='yrwzbbwF8OiYatgy6ena')
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[0-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = 'bd'
password = 'makarenko'
database = 'localhost/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()



print('1.Вивести кількість платних додатків по кожній категорії. \n')
category=[]
count=[]
query1 = '''
SELECT category_name, COUNT(app_name) app_count
FROM Apps
WHERE price!=0
GROUP BY category_name
ORDER BY  app_count,category_name
'''

cursor.execute(query1)

for row in cursor.fetchall():
    category.append (row[0])
    count.append(row[1])
bar = go.Bar (x = category, y = count)
bar = py.plot([bar],auto_open = True, file_name = "Plot1")




print("\n2. Вивести відстоткове відношення додатків по аудиторії людей.\n")
audience=[]
apps=[]
query2 = """
SELECT audience_name , round((COUNT(app_name))/ (SELECT COUNT(*) FROM App)*100, 2)  persent                                                                                                             
FROM Apps
GROUP BY audience_name
ORDER BY persent DESC, audience_name
"""
cursor.execute(query2)
for row in cursor.fetchall():
    audience.append (row[0])
    apps.append(row[1])
pie = go.Pie (labels = audience, values = apps)
pie = py.plot([pie],auto_open = True, file_name = "Plot2",)




print("\nВивести динаміку залежності кількості відгуків додатків від їх ціни, які передбачені для всіх груп користувачів. \n")
reviews=[]
price=[]
query3 = """
SELECT price, SUM(reviews) sum_reviews
FROM Apps
WHERE audience_name='Everyone'
GROUP BY price
ORDER BY price
"""
cursor.execute(query3)

for row in cursor.fetchall():
    reviews.append (row[0])
    price.append(row[1])
scatter = go.Scatter (x = reviews, y = price)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3")



my_dboard = dash.Dashboard()
bar_id = fileId_from_url(bar)
pie_id =fileId_from_url(pie)
scatter_id = fileId_from_url(scatter)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'Вивести кількість платних додатків по кожній категорії.'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': 'Вивести відстоткове відношення додатків по аудиторії людей.'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': 'Вивести динаміку залежності кількості відгуків додатків від їх ціни, які передбачені для всіх груп користувачів.'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)


py.dashboard_ops.upload(my_dboard, 'db_alla_lab3')


cursor.close()
connection.close()


