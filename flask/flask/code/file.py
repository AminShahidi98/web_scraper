#imports -----------------------------------------------------------------------
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs
from booklist import books
import sqlite3
from flask import Flask, render_template
#scraping part -----------------------------------------------------------------
print('getting requirements ready...\n')
def simple_get(url):
    try:
        with closing(get(url,stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except:
        print('Error during requests\nCheck your connection status')
        return None
def is_good_response(resp):
    content_type = resp.headers['content-type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def lener(b):
    l=[]
    rh=simple_get(b)
    html = bs(rh, 'html.parser')
    for span in html.select('span'):
        l.append(span.text)
    l.reverse()
    l=l[17:21]
    for t in html.select('title'):
        l.append(t.text)

        return(l)
print('requirements are ready\n')
#database part -----------------------------------------------------------------
print('Getting database ready...\n')
db = sqlite3.connect('c:/Users/Microsoft/Desktop/flask/code/mtpdb.db')
print('Database created in c:/Users/Microsoft/Desktop/flask/code/mtpdb.db\n')
print('Adding data to database...\nIt may take a while\nData will retrived from internet\n')
cursor=db.cursor()
print('Creating main table at database...\n')
cursor.execute('''CREATE TABLE maint(code INTEGER PRIMARY KEY,name TEXT)''')
count=1
for book in books:
    code=count
    bookname=(lener(book)[4])
    cursor.execute("INSERT INTO maint (code,name) VALUES (?, ?)",(code,bookname))
    count+=1
print('Main table created\n')
print('Creating books price list table...\n')
count=1
cursor.execute('''CREATE TABLE plist (code INTEGER PRIMARY KEY,price TEXT)''')
for book in books:
    code=count
    price=(lener(book)[0])
    cursor.execute("INSERT INTO plist (code,price) VALUES (?, ?)",(code,price))
    count+=1
print('Books price list table created\n')
print('Creating books details table...\n')
count=1
cursor.execute('''CREATE TABLE details (code INTEGER PRIMARY KEY,numberofpages TEXT,translator TEXT,author TEXT)''')
for book in books:
    code=count
    pages=(lener(book)[1])
    translator=(lener(book)[2])
    author=(lener(book)[3])
    cursor.execute("INSERT INTO details (code,numberofpages,translator,author) VALUES (?, ?, ?, ?)",(code,pages,translator,author))
    count+=1
print('Books details table created\n')
db.commit()
print('Database is ready and Data inserted to it')
printcheck=input('If you want to see database enter yes then press enter:')
if printcheck == ('yes') or printcheck == ('Yes') or printcheck == ('YES'):
    print('this is your main table contents:\n')
    cursor.execute('SELECT * FROM maint')
    data=cursor.fetchall()
    for row in data:
        print(row[0],row[1])
    print('this is your books price table contents:\n')
    cursor.execute('SELECT * FROM plist')
    data=cursor.fetchall()
    for row in data:
        print(row)
    print("this is your books detail table contents:\n")
    cursor.execute('SELECT * FROM details')
    data=cursor.fetchall()
    for row in data:
        for i in row:
            print(i)
contin=input('Press eny key to continue...') 


    









    
