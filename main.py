

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
SELECT audience_type , round((COUNT(app_name))/ (SELECT COUNT(*) FROM App)*100, 2)  persent                                                                                                             
FROM Apps
GROUP BY audience_type
ORDER BY persent DESC, audience_type
"""
cursor.execute(query2)
for row in cursor.fetchall():
    audience.append (row[0])
    apps.append(row[1])
pie = go.Pie (labels = audience, values = apps)
pie = py.plot([pie],auto_open = True, file_name = "Plot2",)





my_dboard = dash.Dashboard()
bar_id = fileId_from_url(bar)
pie_id =fileId_from_url(pie)

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


py.dashboard_ops.upload(my_dboard, 'db_alla_lab3')


cursor.close()
connection.close()


