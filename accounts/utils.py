from django.contrib.sites.shortcuts import get_current_site
from .tokens import ConfirmEmailTokenGenerator


confirm_email_token_generator = ConfirmEmailTokenGenerator()

def send_confirmation_email(user):
    token = make_token(user)
    uid = user.id
    domain = get_current_site
    slash = '/'

    subject = 'Activate your account'
    message = f'''
    Please click on the link below to activate your account
     {domain}{slash}{uid}{slash}{token}
    '''

    user.email_user(subject, message)
