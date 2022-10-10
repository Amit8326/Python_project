from flask import *
import pymysql

db=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project"
    )

cursor=db.cursor()

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    telephone=[8996468847]
    return render_template("contact.html", telephone=telephone)

@app.route("/about")
def about():
    founder="founder"
    cofounder="Mangesh ghuge"
    vice="shivajinagar,deccan,pune"
    pin= [411046]
    president="cofounder"
    vicepresident="Santosh singh"
    add="pune"
    code= [415507]
    
    return render_template("about.html",founder=founder, cofounder=cofounder, vice=vice, pin=pin, president=president, vicepresident=vicepresident, add=add, code=code)


@app.route("/alluser")
def alluser():
    cursor.execute("select * from student")
    data=cursor.fetchall()
    return render_template("alluser.html", userdata=data)

@app.route("/create",methods=["POST"])
def create():
    uname=request.form.get('student_name')
    pwd=request.form.get('roll_no')
    contact=request.form.get('total_marks')
    insq="insert into student(student_name,roll_no,total_marks)values('{}','{}','{}')".format(uname,pwd,contact)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('alluser'))
    except:
        db.rollback()
        return "Error in Querry"

@app.route("/delete")
def delete():
    id=request.args.get('id')
    delq = "delete from student where id={}".format(id)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for('alluser'))
    except:
        db.rollback()
        return "Error in Querry"
    
@app.route("/edit")
def edit():
    id = request.args.get('id')
    selq = "select * from student where id={}".format(id)
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("edit.html",row=data)

@app.route("/update",methods=["POST"])
def update():
    uname=request.form.get('student_name')
    pwd=request.form.get('roll_no')
    contact=request.form.get('total_marks')
    id=request.form.get('uid')
    updq="update student set student_name='{}',roll_no='{}',total_marks='{}' where id='{}'".format(uname,pwd,contact,id)
    try:
        cursor.execute(updq)
        db.commit()
        return redirect(url_for('alluser'))
    except:
        db.rollback()
        return "Error in Querry"


if __name__=="__main__":
    app.run(debug=True)