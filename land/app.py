from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from passlib.hash import pbkdf2_sha256
from functools import wraps
from flaskext.mysql import MySQL
import pymysql
from flask_mysqldb import MySQL
# # # from mysql.connector import error
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from flask_table import Table, Col





app = Flask(__name__)
app.secret_key = "super secret key"


class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "5432"
        db = "landbro"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                               DictCursor)
        self.cur = self.con.cursor()

    # def list_nairobi(self):
    #     self.cur.execute("SELECT  * FROM nairobi WHERE constituency, size, price, phone)
    #     result = self.cur.fetchall()

        # cur= mysql.conection.cursor()








 # Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5432'
app.config['MYSQL_DB'] = 'landbro'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MYSQL(app)



# # # init MYSQL
# db = SQLAlchemy(app)

# #Articles = Articles()

# Index
@app.route('/home')
def home():
    return render_template("home.html")

# About
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/SELL')
def sell():
    return render_template('sell.html')

@app.route('/BUY')
def buy():
    return render_template('BUY.html') 

@app.route('/LEASE')
def lease():
    return render_template('lease.html') 

# @app.route('/NAIROBI')
# def nairobi():
    
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM nairobi)
#     data = cur.fetchall()
#     cur.close()

#     return render_template('nairobi.html', nairobi = data)
    

@app.route('/NAIROBI_LEASE')
def nairobi_lease():
        return render_template('nairobi_lease.html')



# @app.route('/nairobi')
# def nairobi();
    







# @pp.route('nairobi')       


# class User(db.model):
#     id = db.column(db.integer, primary_key=True)
#     Username = db.Column(db.String(50), unique=True)
#     phone = db.column(db.Int(15), unique=True)

#     def __init__(self, username, phone):
#         self.username = username
#         self.phone = phone

#     def __repr__(self):
#         return 'User %r>' % self.username    




# @app.route('/BUY')
# def buy():
#    cur = mysql.connection.cursor()
#    resultValue > cur.execute("SELECT * FROM lands")
#    if resultValue > 0:
#        userDetails = cur.fetchall()
#        return render_template("home.html")

# Articles 
# @app.route('/nairobi')
# def lands():
#     # Create cursor
#     cur = mysql.connection.cursor()

#     # Get articles
#     result = cur.execute("SELECT * FROM lands")

#     articles = cur.fetchall()

#     if result > 0:
#         return render_template('nairobi.html', lands=lands)
#     else:
#         msg = 'No Articles Found'
#         return render_template('nairobi.html', msg=msg)
#     # Close connection
#     cur.close()


# # #Single Article
# # @app
# .route('/
# article/<string:id>/')
# # def article(id):
# #     # Create cursor
# #     cur = mysql.connection.cursor()

#     # Get article
#     result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

#     article = cur.fetchone()

#     return render_template('article.html', article=article)


# #  #Register Form Class
# class RegistrationForm(Form):
#     name = StringField('name', [validators.Length(min=2, max=20)])
#     phone = StringField('phone', [validators.Length(min=6, max=50)])
#     password = PasswordField('New Password', [
#         validators.Required(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')


# '''Register Form Class'''
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    phone = StringField('Phone', [validators.Length(min=4, max=11)])
    
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# User Register
@app.route('/register', methods=['GET',  'POST',])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        phone = form.phone.data
        password = form.password.data
        confirm = request.form.get("confirm")
        # password = sha256_crypt.encrypt(str(form.password.data)

        # print("I am here")
        # Create cursor
        cur = mysql.connection.cursor()
        cur = con.cursor()

        # print("cursor", cur)

        # Execute query
        cur.execute("INSERT INTO users(name, phone) VALUES(%s, %s)", (name, phone)) 

        # Commit to DB
        con.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        redirect(url_for('home'))

        
    return render_template("register.html", form=form)

 # @app.route('/register', methods=['POST'])

 # def register():
 #     form = RegistrationForm(request.form)
 #     if request.method == 'POST' and form.validate():
 #         user = User(form.name.data, form.phone.data, form.password.data)
 #         db_session.add(user)
 #         flash('Thanks for registering')
 #         return redirect(url_for('login'))
 #     return render_template('register.html', form=form)        


    

# v
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
 
    if request.method == 'POST':
        # Get Form Fields
        name = request.form['name']
        phone = request.form['phone']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result =  cur.execute("SELECT INTO users(name, phone) VALUES(%s, %s)", (name, phone)) 

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['name'] = name

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')




    # @app.route('/NAIROBI')
    # def nairobi():


    #     cur = con.cursor()
    #     cur.execute("SELECT * FROM nairobi")
    #     data = cur.fetchall()
    #     render_template('nairobi.html', data=data)




    # if request.method == 'GET':
    #     # Get Form Fields
    #     name = request.form['name']
    #     phone = request.form['phone']
        
    #     password_candidate = request.form['password']

        # # Create cursor
        # cur = mysql.connection.cursor()

        # # Get user by username
        # result =  cur.execute("SELECT * FROM nairobi) 

        # if result > 0:
        #     # Get stored hash
        #     data = cur.fetchall()
            

          
        # return render_template('nairobi.html')




# Check if user logged in
# def is_logged_in(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash('Unauthorized, Please login', 'danger')
#             return redirect(url_for('login'))
#     return wrap

# # Logout
# @app.route('/logout')
# @is_logged_in
# def logout():
#     session.clear()
#     flash('You are now logged out', 'success')
#     return redirect(url_for('login'))

# # # Dashboard
# @app.route('/BUY)

# def BUY():
#     # Create cursor
#     cur = mysql.connection.cursor()

#     #et articles
#     result = cur.execute("SELECT * FROM lands)
#     # Show articles only from the user logged in 
#     # result = cur.execute("SELECT * FROM lands author = %s", [session['username']])

#     lands.fetchall()

#     if result > 0:
#         return render_template('buy.html')
#     else:
#         msg = 'No  lands found'
#         return render_template('buy.html')
#     # Close connection
#     cur.close()

# c# Article Form Class
# lass ArticleForm(Form):
#     title = StringField('Title', [validators.Length(min=1, max=200)])
#     body = TextAreaField('Body', [validators.Length(min=30)])

# Dashboard
# 


# class Results(Table):
#     id = ('Id')
#     constituency = ('constituency')
#     size = ('size')
#     price = ('price')
#     phone = ('Phone')
    

# nairobi Form Class
# class ArticleForm(Form):
#     title = StringField('Title', [validators.Length(min=1, max=200)])
#     body = TextAreaField('Body', [validators.Length(min=30)])

# Add land
# @app.route('/add_land', methods=['GET', 'POST'])
# # @is_logged_in
# def add_article():
#     form = nairobiForm(request.form)
#     if request.method == 'POST' and form.validate():
#         title = form.title.data
#         body = form.body.data

#         # Create Cursor
#         cur = mysql.connection.cursor()

#         # Execute
#         cur.execute("INSERT INTO nairobi(photo, constituency, size, phone, price) VALUES(%s, %s, %s, %s, %s)",(title, body, session['username']))

#         # Commit to DB
#         mysql.connection.commit()

#         #Close connection
#         cur.close()

#         flash('Article Created', 'success')

#         return redirect(url_for('nairobi'))

#     return render_template('add_lands.html', form=form)


# # Edit Article
# @app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
# @is_logged_in
# def edit_article(id):
#     # Create cursor
#     cur = mysql.connection.cursor()

#     # Get article by id
#     result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

#     article = cur.fetchone()
#     cur.close()
#     # Get form
#     form = ArticleForm(request.form)

#     # Populate article form fields
#     form.title.data = article['title']
#     form.body.data = article['body']

#     if request.method == 'POST' and form.validate():
#         title = request.form['title']
#         body = request.form['body']

#         # Create Cursor
#         cur = mysql.connection.cursor()
#         app.logger.info(title)
#         # Execute
#         cur.execute ("UPDATE articles SET title=%s, body=%s WHERE id=%s",(title, body, id))
#         # Commit to DB
#         mysql.connection.commit()

#         #Close connection
#         cur.close()

#         flash('Article Updated', 'success')

#         return redirect(url_for('dashboard'))

#     return render_template('edit_article.html', form=form)

# # Delete Article
# @app.route('/delete_article/<string:id>', methods=['POST'])
# @is_logged_in
# def delete_article(id):
#     # Create cursor
#     cur = mysql.connection.cursor()

#     # Execute
#     cur.execute("DELETE FROM articles WHERE id = %s", [id])

#     # Commit to DB
#     mysql.connection.commit()

#     #Close connection
#     cur.close()

#     flash('Article Deleted', 'success')

#     return redirect(url_for('dashboard'))

# #register 2
# @app.route('/register')
# def register():
# 	return render_template('register.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)