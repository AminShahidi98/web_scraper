from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs
from booklist import books
import sqlite3
from flask import Flask, render_template
print('Creating web application...')
database = sqlite3.connect('c:/Users/Microsoft/Desktop/flask/code/mtpdb.db')
c=database.cursor()
c.execute('SELECT * FROM maint')
d=c.fetchall()
c.execute('SELECT * FROM plist')
p=c.fetchall()
c.execute('SELECT * FROM details')
g=c.fetchall()
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',data0=d[0][1],data1=d[1][1],data2=d[2][1],data3=d[3][1],data4=d[4][1],data5=d[5][1],data6=d[6][1],
                           data7=d[7][1],data8=d[8][1],data9=d[9][1],data10=d[10][1],data11=d[11][1],data12=d[12][1],data13=d[13][1],data14=d[14][1],
                           data15=d[15][1],data16=d[16][1],data17=d[17][1],data18=d[18][1],
                           pd0=p[0][1],pd1=p[1][1],pd2=p[2][1],pd3=p[3][1],pd4=p[4][1],pd5=p[5][1],
                           pd6=p[6][1],pd7=p[7][1],pd8=p[8][1],pd9=p[9][1],pd10=p[10][1],pd11=p[11][1],
                           pd12=p[12][1],pd13=p[13][1],pd14=p[14][1],pd15=p[15][1],pd16=p[16][1],pd17=p[17][1],
                           pd18=p[18][1],pg0=g[0][1],pg1=g[1][1],pg2=g[2][1],pg3=g[3][1],pg4=g[4][1],pg5=g[5][1],
                           pg6=g[6][1],pg7=g[7][1],pg8=g[8][1],pg9=g[9][1],pg10=g[10][1],pg11=g[11][1],pg12=g[12][1],
                           pg13=g[13][1],pg14=g[14][1],pg15=g[15][1],pg16=g[16][1],pg17=g[17][1],pg18=g[18][1],tl0=g[0][2],
                           tl1=g[1][2],tl2=g[2][2],tl3=g[3][2],tl4=g[4][2],tl5=g[5][2],tl6=g[6][2],tl7=g[7][2],tl8=g[8][2],
                           tl9=g[9][2],tl10=g[10][2],tl11=g[11][2],tl12=g[12][2],tl13=g[13][2],tl14=g[13][2],tl15=g[15][2],
                           tl16=g[16][2],tl17=g[17][2],tl18=g[18][2],au0=g[0][3],au1=g[1][3],au2=g[2][3],au3=g[3][3],au4=g[4][3],
                           au5=g[5][3],au6=g[6][3],au7=g[7][3],au8=g[8][3],au9=g[9][3],au10=g[10][3],au11=g[11][3],au12=g[12][3],au13=g[13][3],
                           au14=g[14][3],au15=g[15][3],au16=g[16][3],au17=g[17][3],au18=g[18][3],link0=books[0],link1=books[1],link2=books[2],link3=books[3],link4=books[4],link5=books[5],
                           link6=books[6],link7=books[7],link8=books[8],link9=books[9],link10=books[10],link11=books[11],link12=books[12],link13=books[13],link14=books[14],link15=books[15],
                           link16=books[16],link17=books[17],link18=books[18],)
if __name__=='__main__':
    app.run(debug=True)
    
