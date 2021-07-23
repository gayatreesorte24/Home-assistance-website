from flask import Flask, render_template, request

from dbconnect import Database

app=Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/doStoreLogin',methods=['POST','GET'])
def doStoreLogin():
    if request.method=='POST':
        name = request.form['Username']
        email=request.form['email']
        passw1=request.form['password1']
        passw2=request.form['password2']
        if passw1 != passw2:
            message="Password do not match !!"
        else:
            db=Database()
            if db.storeLogin(name, email, passw1)==True:
                message="Signup Successful !!"
            else:
                message="Sigup failed !!"
            db.die()
    return render_template('login.html', m=True)

@app.route('/doCheckLogin',methods=['POST','GET'])
def doCheckLogin():
    if request.method=='POST':
        username=request.form['Username']
        passw=request.form['password']
        db=Database()
        if db.checkLogin(username,passw)==True:
            return render_template('userhome.html')
        else:
            message="Login failed !!"
        db.die()
    return render_template('userhome.html', m=True)




@app.route('/thank')
def thank():

    return render_template('thank.html')

@app.route('/userhome')
def userhome():
    return render_template('userhome.html')


if __name__ == '__main__':
    app.run( debug=True )