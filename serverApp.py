from flask import Flask, render_template, url_for, redirect, request, flash

#------------------------------------------------------>
#------------------------------------------------------>


app = Flask( __name__ )

app.secret_key="KingDevelopment"


#------------------------------------------------------>
#------------------------------------------------------>


@app.route( '/' )

def index():
    return render_template( 'App/auth/index.html' )


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

    

    if len( password ) < 6 or len( password2 ) < 6:
        flash( 'Password must be have 6 or more characters' )
        return redirect( url_for( 'startRegister' ) )


    if password != password2:
            flash( 'Passwords must be the same' )
            return redirect( url_for( 'startRegister' ) )



    if len( userName ) < 4:
        flash( 'User name must be have 4 or more characters' )
        return redirect( url_for( 'startRegister' ) )



    if email.find( '@' ) == -1 or email.find( '.' ) == -1:
        flash( 'An email is required' )
        return redirect( url_for( 'startRegister' ) )


    return userName


##########################################################


@app.route( '/home' )

def home():
    return render_template( 'App/home/home.html' )


#------------------------------------------------------>
#------------------------------------------------------>

if __name__ == '__main__':
    app.run( port = 3000, debug = True )