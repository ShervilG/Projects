from flask import Flask,render_template,url_for,request
app = Flask(__name__)
import sqlite3
import os.path

#global variables
gno = int()
bno = int()
date = str()
bill_info_price = []
gno1 = int()
bno1 = int()
date2 = str()
bill_info_price1 = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "bill_managment2.db")
 
@app.route("/")
def intro():
    return render_template('add_me.html')

@app.route("/first")
def login():
    return render_template('first_page.html')

@app.route("/check",methods = ['POST','GET'])
def check():
    username = request.form['username']
    psw = request.form['psw']
    if username == "admin" and psw == "admin":
        return render_template("main_menu.html")
    else:
        return ("Wrong username/password")
@app.route("/party1")
def purchase():
    return render_template('party_type.html')
@app.route("/customer")
def sell():
    return render_template('customer_type.html')
@app.route("/bill")
def bill():
    return render_template('Bill.html')
@app.route("/add_raw")
def raw():
    return render_template('Material.html')
@app.route("/add_product")
def product():
    return render_template('Product.html')
@app.route("/purchase")
def purchase1():
    return render_template('new_party.html')
@app.route("/old_party")
def old_party():
    return render_template('old_party.html')
@app.route("/Sell")
def Sell():
    return render_template('new_customer.html')
@app.route("/old_customer")
def old_customer():
    return render_template('old_customer.html')

@app.route("/save_old",methods = ['GET','POST'])
def add_data01():
    global gno1
    global bno1
    global date2
    gno1 = request.form['gst']
    bno1 = request.form['bno']
    date2 = request.form['date']
    mon = request.form['month']
    year = request.form['year']
    date2 = year+"-"+mon+"-"+date2
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("select * from customer where gstno_pt = ?",(gno1,))
    d = c.fetchall()
    if len(d)==0:
        return "no such customer !!"
    else:
        return render_template('Product_info.html') #yaha se continue

@app.route("/old1",methods = ['GET','POST'])
def add_data1():
    global gno
    global bno
    global date
    gno = request.form['gno']
    bno = request.form['bno']
    date1 = request.form['date']
    mon = request.form['month']
    year = request.form['year']
    date = year+"-"+mon+"-"+date1
    conn = sqlite3.connect(db_path)
    c = conn.cursor()#object of connection used to execute queries
    c.execute("select * from partyinfo where Gst_no_raw = ?",(gno,))
    d = c.fetchall()
    if len(d)==0:
        return "error, no such party exists !!"
    else:
        return render_template('Material_info.html') #yaha se continue

@app.route("/old2",methods = ['GET','POST'])
def add_data2():
    global bno
    global gno
    global date
    global bill_info_price
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    mat_name = request.form['name']
    mat_price = request.form['price']
    mat_id = 1
    c.execute('select count(*) from Rawmaterial')
    d = c.fetchall()
    if len(d)==0:
        mat_id = 1
    else:
        for x in d:
            mat_id = int(x[0]) + 1
    c.execute('insert into Rawmaterial values(?,?,?)',(mat_id,mat_name,mat_price,))
    mat_qty = request.form['qty']
    total_qty = int(mat_qty) * int(mat_price)
    bill_info_price.append(total_qty)
    #conn.commit()
    c.execute('insert into bill_details1 values(?,?,?,?)',(mat_id,mat_qty,total_qty,bno,))   
    conn.commit()
    return render_template('Material_info.html')

@app.route("/finalize",methods=['POST','GET'])
def add_data3():
    global bno
    global gno
    global date
    global bill_info_price
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    sum1 = 0
    for i in bill_info_price:
        sum1 += i
    c.execute('insert into bill_information1 values(?,?,?,?)',(date,bno,sum1,gno,)) 
    conn.commit()
    bill_info_price = []
    return '''<html><p>success!!</p><a href = "/main1">back</a></html>'''

@app.route("/main1")
def dadadada():
    return render_template("main_menu.html")


@app.route("/add_mat",methods=['POST','GET'])
def add_mat():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    mat_name = request.form['mname']
    mat_price = request.form['price']
    mat_id = 1
    c.execute('select count(*) from Rawmaterial')
    d = c.fetchall()
    if len(d)==0:
        mat_id = 1
    else:
        for x in d:
            mat_id = int(x[0]) + 1
    c.execute('insert into Rawmaterial values(?,?,?)',(mat_id,mat_name,mat_price,))
    conn.commit()
    return '''<html><p>success!!</p><a href = "/main1">back</a></html>'''

@app.route("/add_product",methods=['POST','GET'])
def add_pro():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    mat_name = request.form['pname']
    mat_price = request.form['price']
    mat_id = 1
    c.execute('select count(*) from Product_details')
    d = c.fetchall()
    if len(d)==0:
        mat_id = 1
    else:
        for x in d:
            mat_id = int(x[0]) + 1
    c.execute('insert into Product_details values(?,?,?)',(mat_id,mat_name,mat_price,))
    conn.commit()
    return '''<html><p>success!!</p><a href = "/main1">back</a></html>'''

@app.route("/newp",methods=['POST','GET'])
def new_party():
    global gno
    global bno
    global date
    name = request.form['t1']
    address = request.form['t2']
    number = request.form['t3']
    gno = request.form['t4']
    bno = request.form['t5']
    date1 = request.form['date']
    month = request.form['month']
    year = request.form['year']
    date = year+"-"+month+"-"+date1
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('insert into Partyinfo values(?,?,?,?)',(address,gno,name,number))
    conn.commit()
    return render_template('Material_info.html')


@app.route("/newcust",methods=['POST','GET'])
def new_customer():
    global gno1
    global bno1
    global date2
    name = request.form['t1']
    address = request.form['t2']
    number = request.form['t3']
    gno1 = request.form['t4']
    bno1 = request.form['t5']
    date2 = request.form['date']
    month = request.form['month']
    year = request.form['year']
    date2 = year+"-"+month+"-"+date2
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('insert into Customer values(?,?,?,?)',(gno1,address,number,name))
    conn.commit()
    return render_template('Product_info.html')

@app.route("/p_info",methods=['POST'])
def product_iter():
    global bno1
    global gno1
    global date2
    global bill_info_price1
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    mat_name = request.form['name1']
    mat_price = request.form['price1']
    mat_id = 1
    c.execute('select count(*) from Product_details')
    d = c.fetchall()
    if len(d)==0:
        mat_id = 1
    else:
        for x in d:
            mat_id = int(x[0]) + 1
    c.execute('insert into Product_details values(?,?,?)',(mat_id,mat_name,mat_price,))
    mat_qty = request.form['qty1']
    total_qty = int(mat_qty) * int(mat_price)
    bill_info_price1.append(total_qty)
    #conn.commit()
    c.execute('insert into Bill_Detail values(?,?,?,?)',(mat_id,mat_qty,total_qty,bno1,))
    conn.commit()
    return render_template('Product_info.html')

@app.route("/finalize_product",methods=['POST','GET'])
def add_data31():
    global bno1
    global gno1
    global date2
    global bill_info_price1
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    sum1 = 0
    for i in bill_info_price1:
        sum1 += i
    c.execute('insert into bill_information values(?,?,?,?)',(sum1,bno1,gno1,date2,)) 
    conn.commit()
    bill_info_price1 = []
    return '''<html><p>success!!</p><a href = "/main1">back</a></html>'''

@app.route("/magic",methods=['POST'])
def make_dat_shit():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    bno = request.form['t1']
    date = str()
    gno = str()
    total_price = int()
    party_info = []
    cust_info = []
    c.execute('select * from bill_information1 where bill_no_raw = ?',(bno,))
    d = c.fetchall()
    if len(d)==0:
        c.execute('select * from bill_information where bill_no_pt = ?',(bno,))
        d = c.fetchall()
        for x in d:
            date1 = str(x[3])
            bno = str(x[1])
            total_price = int(x[0])
            gno = str(x[2])
        c.execute('select * from customer where gstno_pt = ?',(gno,))
        d = c.fetchall()
        if len(d)==0:
            return "no such customer !!"
        else:
            for x in d:
                for i in x:
                    cust_info.append(i)
        c.execute('select product_id,Quantity_pt,Totalproductprice from bill_detail where bill_no_pt = ?',(bno,))
        d = c.fetchall()
        print(len(d))
        mat_details = {}
        mat_details2 = {}
        for x in d:
            mat_details[x[0]] = [x[1],x[2]]
        for mat_id in list(mat_details.keys()):
            c.execute('select * from product_details where product_id = ?',(mat_id,))
            d = c.fetchall()
            for x in d:
                mat_details2[mat_id] = [x[1],x[2]]
            for id in list(mat_details2.keys()):
                mat_details2[id] += mat_details[id]
                print(mat_details2[id])
        return render_template("dynamic_bill1.html",cust_info=cust_info,bno=bno,gno=gno,lis2=mat_details2,dd=total_price,date1=date1) 
    #else for party wala case
    else:
        for x in d:
            date1 = str(x[0])
            bno = str(x[1])
            total_price = int(x[2])
            gno = str(x[3])
    c.execute('select * from Partyinfo where Gst_no_raw = ?',(gno,))
    d = c.fetchall()
    if len(d)==0:
        return "no such party !!"
    else:
        for x in d:
            for i in x:
                party_info.append(i)
    c.execute('select Material_id,Quantity_raw,Totalmaterialprice from bill_details1 where bill_no_raw = ?',(bno,))
    d = c.fetchall()
    print(len(d))
    mat_details = {}
    mat_details2 = {}
    for x in d:
        mat_details[x[0]] = [x[1],x[2]]
    for mat_id in list(mat_details.keys()):
        c.execute('select * from Rawmaterial where Material_id = ?',(mat_id,))
        d = c.fetchall()
        for x in d:
            mat_details2[mat_id] = [x[1],x[2]]
    for id in list(mat_details2.keys()):
        mat_details2[id] += mat_details[id]
        print(mat_details2[id])
    return render_template("dynamic_bill.html",party_info=party_info,bno=bno,gno=gno,lis2=mat_details2,dd=total_price,date1=date1)



if __name__ == "__main__":
    app.run()
