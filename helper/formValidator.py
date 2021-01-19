
def registerValidator( formValues = {} ):

    msg = ''

    if formValues['password'] != formValues['password2']:

        msg = 'Passwords must be the same'
        return msg

    elif len( formValues['password'] ) < 6:

        msg = 'Password must be have 6 or more characters'
        return msg

    elif len( formValues['userName'] ) < 4:

         msg = 'User name must be have 4 or more characters' 
         return msg

    elif formValues['email'].find( '@' ) == -1 or formValues['email'][-7::].find( '.' ) == -1:
        
        msg = 'An email is required'
        return msg 
        
    else:

        msg = 'ok'
        return msg
  


###################################################################################



def loginValidator( formValues = {} ):

    msg = ''


    if len( formValues['userName'] ) < 4:

        msg = 'User name must be have 4 or more characters' 
        return msg


    elif len( formValues['password'] ) < 6:

         msg = 'Password must be have 6 or more characters'
         return msg


    else:

        msg = 'ok'
        return msg