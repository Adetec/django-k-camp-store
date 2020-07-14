


def send_confirmation_email(user):
    token = make_token(user)
    uid = user.id
    domain = 'http://localhost:8000'
    slash = '/'

    subject = 'Activate your account'
    message = f'''
    Please click on the link below to activate your account
     {domain}{slash}{uid}{slash}{token}
    '''

    user.email_user(subject, message)
