from flask import Flask, render_template, url_for, redirect, request, flash, session
from helper import formValidator
from flaskext.mysql import MySQL, pymysql
import bcrypt

#------------------------------------------------------>
#------------------------------------------------------>


app = Flask( __name__ )

app.secret_key="KingDevelopment"


#------------------------------------------------------>
#------------------------------------------------------>


mysql = MySQL()
app.config[ 'MYSQL_DATABASE_HOST' ]     = 'den1.mysql2.gear.host' 
app.config[ 'MYSQL_DATABASE_USER' ]     = 'sessiondb' 
app.config[ 'MYSQL_DATABASE_PASSWORD' ] = 'Yi4p8?sJ88?J' 
app.config[ 'MYSQL_DATABASE_DB' ]       = 'sessiondb' 
mysql.init_app( app )


#------------------------------------------------------>
#------------------------------------------------------>


@app.route( '/' )

def startLogin():

    try:

        session[ 'username' ]
        return redirect( url_for( 'home' ) )

    except KeyError as error:

        print( error )
        return render_template( 'App/auth/login.html' )

    
#-----------------------------------------------------------|


@app.route( '/login', methods = [ 'POST' ] )

def login():

    userName  = request.form[ 'userName' ]
    password  = request.form[ 'password' ]

    res = formValidator.loginValidator( { 'userName' : userName, 'password' : password } )

    if res != "ok":


        flash( res )
        return redirect( url_for( 'startLogin' ) )


    else:

       
        query = "SELECT * FROM users WHERE userName = %s"
        data = ( userName )

        conn = mysql.connect()
        cursor = conn.cursor()


        try:

            msg = ''

            cursor.execute( query, data )
            conn.commit()
            response = cursor.fetchall()


            if len( response ) == 0:

                flash( 'User name or password are incorret' )
                return redirect( url_for( 'startLogin' ) )



            if not bcrypt.checkpw( password.encode( 'utf-8' ), response[0][3].encode( 'utf-8' )  ):

               flash( 'User name or password are incorret' )
               return redirect( url_for( 'startLogin' ) )
            

            session[ 'username' ] = response[0][1]
            return redirect( url_for( 'home' ) )


        except ( pymysql.err.IntegrityError ) as error:

            print( error )
            
            flash( 'Please contact to administrator' )
            return redirect( url_for( 'startLogin' ) )

            
##########################################################


@app.route( '/startregister' )

def startRegister():
    return render_template( 'App/auth/register.html' )


#-----------------------------------------------------------|


@app.route( '/register', methods = [ 'POST' ] )

def register():
    
    userName  = request.form[ 'userName' ]
    email     = request.form[ 'email' ]
    password  = request.form[ 'password' ]
    password2 = request.form[ 'password2' ]


    res = formValidator.registerValidator( { 'userName' : userName, 'email' : email, 'password' : password, 'password2' : password2 } )


    if res != 'ok':

        flash( res )
        return redirect( url_for( 'startRegister' ) )
    
    else:

        PassHashed = bcrypt.hashpw( password.encode( 'utf-8' ), bcrypt.gensalt() )

        query = "INSERT INTO users ( userName, email, password ) VALUES ( %s, %s, %s );"
        data = ( userName.capitalize(), email, PassHashed )

        conn = mysql.connect()
        cursor = conn.cursor()
       

        try:

            cursor.execute( query, data )
            conn.commit()

            flash( 'Your account has been created successfully' )
            return redirect( url_for( 'startRegister' ) )


        except ( pymysql.err.IntegrityError ) as error:

           
            print( error )
            
            msg = 'Please contact to administrator'

           
            if str( error ).find( "emial_UNIQUE" ) != -1:
                msg = 'Email is already taken'


            if str( error ).find( "userName_UNIQUE" ) != -1:
                msg = 'User name is already taken'
            

            flash( msg )
            return redirect( url_for( 'startRegister' ) )


##########################################################


@app.route( '/home' )

def home():

    try:

        session[ 'username' ]
        return render_template( 'App/home/home.html' )

    except KeyError as error:

        print( error )
        return redirect( url_for( 'startLogin' ) )


##########################################################


@app.route( '/logout' )

def logout():

    session.pop( 'username', None  )
    return redirect( url_for( 'startLogin' ) )


#------------------------------------------------------>
#------------------------------------------------------>

if __name__ == '__main__':
    app.run( port = 3000, debug = True )