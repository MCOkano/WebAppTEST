from flask import Flask,render_template,request

import pyodbc

server = 'mcdev001.database.windows.net'
database = 'DMRE_Demo_1st'
username = 'mcroot'
password = 'mlG0klf$3_6r'   
driver= '{ODBC Driver 17 for SQL Server}'

def connectSQL():

    server = 'mcdev001.database.windows.net'
    database = 'DMRE_Demo_1st'
    username = 'mcroot'
    password = 'mlG0klf$3_6r'   
    driver= '{ODBC Driver 17 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    print("SQL Connect OK")
    return conn,cursor

def closeSQL(_cursor,_conn):
    _cursor.close()
    _conn.close()
    print("SQL Close OK")
    return

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main_page_GET():
    text = "ここに結果が出力されます"
    return render_template("page.html",text=text)

@app.route("/", methods=["POST"])
def main_page_POST():
    name = request.form["name"]

 #   cn,cur = connectSQL()

 #   cur.execute("select * from Tbl_D_注文書番号")
 #   rows = cur.fetchall()

 #   closeSQL(cur,cn)
    rows = [['0','Aa'],['1','Bb'],['2','Cc'],['3','D'],['4','E'],['5','F'],['2','G']]

    rows2 = []

    list = []

    text = "該当データなし"
    str1 = "文字列2"
    for r in rows:
        print("r[0] " + r[0])
        print("name " + name)
        if name == r[0]:
            text = "選択ID：" + name + "    該当内容：" + r[1]
            list.append(text)
            text2 = r[0] , r[1]
            rows2.append(text2)
            print(list)
            print(rows2)
#            break

    return render_template("page2.html",text=text,str1=str1,arr=rows,arr2=rows2,list=list)

## 実行
if __name__ == "__main__":
    app.run(debug=True)