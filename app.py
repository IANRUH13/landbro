from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
# from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField
from passlib.hash import pbkdf2_sha256
from functools import wraps
from flaskext.mysql import MySQL
import pymysql
from flask_mysqldb import MySQL
from mysql.connector import Error
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from flask_table import Table, Col
import mysql.connector
from passlib.hash import sha256_crypt
import bcrypt





app = Flask(__name__)
app.secret_key = "super secret key"


class Database:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = "5432"
        db = "landbr"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                               DictCursor)
        self.cur = self.con.cursor()


    def list_landbro(self):
        self.cur.execute("SELECT * FROM nairobi WHERE constituency, size, price, phone")
        res= self.cur.fetchall()

        return res

        

      



mySQLconnection = mysql.connector.connect(host='localhost',
                             database='landbro',
                             user='root',
                             password='5432')




 # Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'landbro'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_DATABASE_CHARSET']='utf-8'
# app.config['MYSQL_PASSWORD'] = '5432'

# mysql.init_app(app) 
mysql = MySQL(app)

# mysql = MYSQL(app)


app.config['MYSQL_PASSWORD'] = '5432'

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







@app.route('/NAIROBI')
def nairobi():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nairobi")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nairobi.html', data = fetchdata)


@app.route('/NYERI')
def nyeri():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nyeri")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nyeri.html', data = fetchdata)



@app.route('/NYANDARWA')
def nyandarwa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nairobi")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nyandarwa.html', data = fetchdata)
    
@app.route('/MOMBASA')
def mombasa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mombasa")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('mombasa.html', data = fetchdata)
    
@app.route('/KWALE')
def kwale():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kwale")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kwale.html', data = fetchdata)
    
@app.route('/KILIFI')
def kilifi():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kilifi")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kilifi.html', data = fetchdata)
    
@app.route('/TANARIVER')
def tanariver():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tanariver")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('tanariver.html', data = fetchdata)
    
@app.route('/LAMU')
def lamu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM lamu")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('lamu.html', data = fetchdata)
    
@app.route('/TAITA_TAVETA')
def taita_taveta():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM taita_taveta")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('taita_taveta.html', data = fetchdata)
   
@app.route('/GARISSA')
def garissa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM garissa")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('garissa.html', data = fetchdata)
    
@app.route('/WAJIR')
def wajir():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nairobi")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('wajir.html', data = fetchdata)
    
@app.route('/MANDERA')
def mandera():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mandera")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('mandera.html', data = fetchdata)
    

@app.route('/MARSABIT')
def marsabit():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM marsabit")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('marsabit.html', data = fetchdata)
    
@app.route('/ISIOLO')
def isiolo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM isiolo")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('isiolo.html', data = fetchdata)
    
@app.route('/MERU')
def meru():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM meru")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('meru.html', data = fetchdata)
    
@app.route('/THARAKA')
def tharaka():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tharaka")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('tharaka.html', data = fetchdata)
    
@app.route('/EMBU')
def embu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM embu")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('embu.html', data = fetchdata)
    
@app.route('/KITUI')
def kitui():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kitui")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nairobi.html', data = fetchdata)
    
@app.route('/MACHAKOS')
def machakos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM machakos")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('machakos.html', data = fetchdata)
    
@app.route('/MAKUENI')
def makuenni():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM makueni")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nairobi.html', data = fetchdata)
    
@app.route('/KIRINYAGA')
def kirinyaga():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kirinyaga")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kirinyaga.html', data = fetchdata)
    
@app.route('/MURANGA')
def muranga():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM muranga")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('muranga.html', data = fetchdata)
    
    
@app.route('/KIAMBU')
def kiambu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kiambu")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nairobi.html', data = fetchdata)


@app.route('/WEST_POKOT')
def west_pokot():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM west_pokot")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('west_pokot.html', data = fetchdata)    
    
@app.route('/turkana')
def turkana():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM turkana")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('turkana.html', data = fetchdata)
    
@app.route('/SAMBURU')
def samburu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM samburu")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('samburu.html', data = fetchdata)
    

@app.route('/TRANNSZOIA')
def transzoia():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM transzoia")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('transzoia.html', data = fetchdata)
    

@app.route('/UASIN_GISHU')
def UASIN_GISHU():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM uasin_gishu")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('uasin_gishu', data = fetchdata)
    

@app.route('/ELGEYO_MARAKWET')
def elgeyo_marakwet():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM elgeyo_marakwet")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('elgeyo_marakwet.html', data = fetchdata)
    

@app.route('/NANDI')
def nandi():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nandi")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nandi.html', data = fetchdata)
    

@app.route('/BARINGO')
def baringo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM baringo")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('baringo.html', data = fetchdata)
    

@app.route('/LAIKIPIA')
def laikipia():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM laikipia")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('laikipia.html', data = fetchdata)
    

@app.route('/NAKURU')
def nakuru():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nakuru")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nakuru.html', data = fetchdata)
    

@app.route('/NAROK')
def narok():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM narok")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('narok.html', data = fetchdata)
    

@app.route('/KAJIADO')
def kajiado():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kajiado")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kajiado.html', data = fetchdata)
    

@app.route('/KERICHO')
def kericho():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kericho")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kericho.html', data = fetchdata)
    

@app.route('/BOMET')
def bomet():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bomet")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('bomet.html', data = fetchdata)
    

@app.route('/KAKAMEGA')
def kakamega():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kakamega")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kakamega.html', data = fetchdata)
    

@app.route('/VIHIGA')
def vihiga():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM vihiga")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('vihiga.html', data = fetchdata)
    

@app.route('/BUNGOMA')
def bungoma():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bungoma")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('bungoma.html', data = fetchdata)
    

@app.route('/BUSIA')
def busia():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM busia")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('busia.html', data = fetchdata)
    

@app.route('/SIAYA')
def siaya():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM siaya")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('siaya.html', data = fetchdata)
    

@app.route('/KISUMU')
def kisumu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kisumu")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kisumu.html', data = fetchdata)
    

@app.route('/HOMABAY')
def homabay():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM homabay")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('homabay.html', data = fetchdata)
    

@app.route('/MIGORI')
def migori():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM migori")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('migori.html', data = fetchdata)
    

@app.route('/KISii')
def kisii():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kisii")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('kisii.html', data = fetchdata)
    

@app.route('/NYAMIRA')
def nyamira():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nyamira")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('nyamira.html', data = fetchdata)










# @app.route('/NAIROBI_LEASE')
# def nairobi_lease():

# @app.route('/NYERI_LEASE')
# def nyeri_lease():

# @app.route('/NYANDARWA_LEASE')
# def nyandarwa_lease():
    
# @app.route('/MOMBASA_LEASE')
# def mombasa_lease():
    
# @app.route('/KWALE_LEASE')
# def kwale_lease():
    
# @app.route('/KILIFI_LEASE')
# def kilifi_lease():
    
# @app.route('/TANARIVER_LEASE')
# def tanariver_lease():
    
# @app.route('/LAMU_LEASE')
# def lamu_lease():
    
# @app.route('/TAITA-TAVETA_LEASE')
# def taita-taveta_lease():
   
# @app.route('/GARISA_LEASE')
# def garisa_lease():
    
# @app.route('/WAJIR_LEASE')
# def wajir_lease():
    
# @app.route('/MANDERA_LEASE')
# def mandera_lease():
    

# @app.route('/MARSABIT_LEASE')
# def marsabit_lease():
    
# @app.route('/ISIOLO_LEASE')
# def isiolo_lease():
    
# @app.route('/MERU_LEASE')
# def meru_lease():
    
# @app.route('/THARAKA_LEASE')
# def tharaka_lease():
    
# @app.route('/EMBU_LEASE')
# def embu_lease():
    
# @app.route('/KITUI_LEASE')
# def kitui_lease():
    
# @app.route('/MACHAKOS_LEASE')
# def machakos_lease():
    
# @app.route('/MAKUENI_LEASE')
# def makueni_lease():
    
# @app.route('/KIRINYAGA_LEASE')
# def kirinyaga_lease():
    
# @app.route('/MURANGA')
# def muranga_lease():
    
# @app.route('/NYERI_LEASE')
# def nyeri_lease():
    
# @app.route('/KIAMBU_LEASE')
# def kiambu_lease():
    
# @app.route('/WEST_POKOT')
# def west-pokot_lease():
    
# @app.route('/SAMBURU_LEASE')
# def samburu_lease():
    

# @app.route('/TRANNSZOIA_LEASE')
# def transzoia_lease():
    

# @app.route('/UASIN-GISHU_LEASE')
# def uasin-gishu_lease():
    

# @app.route('/ELGEYO-MARAKWET_LEASE')
# def elgeyo-marakwet_lease():
    

# @app.route('/NANDI_LEASE')
# def nandi_lease():
    

# @app.route('/BARINGO_LEASE')
# def baringo_lease():
    

# @app.route('/LAIKIPIA_LEASE')
# def laikipia_lease():
    

# @app.route('/NAKURU_LEASE')
# def nakuru_lease():
    

# @app.route('/NAROK_LEASE')
# def narok_lease():
    

# @app.route('/KAJIADO_LEASE')
# def kajiado_lease():
    

# @app.route('/KERICHO_LEASE')
# def kericho_lease():
    

# @app.route('/BOMMET_LEASE')
# def bomet_lease():
    

# @app.route('/KAKAMEGA_LEASE')
# def kakamega_lease():
    

# @app.route('/VIHIGA_LEASE')
# def vihiga_lease():
     

# @app.route('/BUNGOMA_LEASE')
# def bungoma_lease():
    

# @app.route('/BUSIA_LEASE')
# def busia_lease():
    

# @app.route('/SIAYA_LEASE')
# def siaya_lease():
    

# @app.route('/KISUMU_LEASE')
# def kisumu_lease():
    

# @app.route('/HOMABAY_LEASE')
# def homabay_lease():
    

# @app.route('/MIGORI_LEASE')
# def migori_LEASE():
    

# @app.route('/KISUMU_LEASE')
# def kisumu_lease():
    

# @app.route('NYAMIRA_LEASE')
# def nyamira_lease():


    










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
        # hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        # password = sha256_crypt.encrypt(str(form.password.data)

        # print("I am here")
        # Create cursor
        cur = mysql.connection.cursor()
        # cur = con.cursor()

        print("cursor", cur)

        # Execute query
        cur.execute("INSERT INTO users(name, phone, password) VALUES(%s, %s, %s)", (name, phone, password)) 

        # Commit to DB
        # conn.commit()
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        redirect(url_for('home'))

        
    return render_template("register.html", form=form)

 

    


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        name = request.form['name']
        print("name", name)
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE phone = %s")
        user = cur.fetchone()
        print(user, "user")
        print(user.get("password"), "password outside")

        if user is not None:
            password_db = user.get("password")
            print(password_db, "db password")
            print(password_candidate, "candidate inside")

            # Compare Passwords
            if (password_db == password_candidate):
                # Passed
                session['logged_in'] = True
                session['name'] = ('name')

                flash('You are now logged in', 'success')
                return render_template('dashboard.html')
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')



#lands single
app.route('/land/<string:id>/')
def land():

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * from lands WHERE id = %s", [id])
    land = cur.fetchone()

    return render_template("land.html")



#lands
@app.route('/lands')
def lands():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM lands")
    lands = cur.fetchall()

    if result is not None:
        return render_template('lands.html, lands=lands')

    else:
        msg = 'no lands found'
        return render_template('lands.html, msg=msg')

    cur.close()            





# Dashboard
@app.route('/dashboard')
# @is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")
    # Show articles only from the user logged in 
    result = cur.execute("SELECT * FROM nairobi")

    lands = cur.fetchall()


    if result is not None: 
        return render_template('dashboard.html', result=result)
    else:
        msg = 'No lands Found'
        return render_template('dashboard.html', msg=msg)
    # Close connection
    cur.close()






# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


    

# nairobi Form Class
class LandForm(Form):
    constituency = StringField('constituency', [validators.Length(min=1, max=200)])
    size = StringField('size', [validators.Length(min=3)])
    price = StringField('price', [validators.Length(min=3)])
    phone = StringField('phone', [validators.Length(min=3)])

# Add land
@app.route('/add_land', methods=['GET', 'POST'])
# @is_logged_in
def add_land():
    form = LandForm(request.form)
    if request.method == 'POST' and form.validate():
        constituency = form.constituency.data
        size = form.size.data
        price = form.price.data
        phone = form.phone.data
       

        # Create Cursor
        cur = mysql.connection.cursor()

        db.lanbro = landbro

        # Execute
        cur.execute("INSERT INTO landbro = %s(constituency, size, price, phone) VALUES(%s, %s, %s, %s)",(constituency, size, price, phone))

        # Commit to DB
        mysql.connection.commit()

        

        #Close connection
        cur.close()


        flash('Your land is succesfully uploaded ', 'success')







    return render_template('add_land.html', form=form)    

#         flash('Article Created', 'success')



#     return render_template('add_lands.html', form=form)

# @app.route('/getsession')
#     def getsession():
#         if 'name' in session
#             return session('name')


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
# @is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article by id
    result = cur.execute("SELECT * FROM nairobi WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()
    # Get form
    form = LandForm(request.form)

    # Populate article form fields
    form.constituency.data = land['constituency']
    form.size.data = land['size']
    form.price.data = land['price']
    form.phone.data = land['phone']

    if request.method == 'POST' and form.validate():
        constituency = request.form['constituency']
        size = request.form['size']
        price = request.form['price']
        phone = request.form['phone']
        # Create Cursor
        cur = mysql.connection.cursor()
        app.logger.info(constituency)
        # Execute
        cur.execute ("UPDATE nairobi SET constituency=%s, size=%s, price=s, phone=%s WHERE id=%s",(constituency, body, id))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('land Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)

# Delete Article
@app.route('/delete_land/<string:id>', methods=['POST'])
@is_logged_in
def delete_land(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("DELETE FROM nairobi WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)