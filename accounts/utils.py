from django.contrib.sites.shortcuts import get_current_site
from .tokens import ConfirmEmailTokenGenerator


confirm_email_token_generator = ConfirmEmailTokenGenerator()

def send_confirmation_email(request, user):
    token = confirm_email_token_generator.make_token(user)
    uid = str(user.id)
    domain = str(get_current_site(request))
    slash = '/'

    subject = 'Activate your account'
    message = f'''
    Please click on the link below to activate your account
     {domain}{slash}{uid}{slash}{token}
    '''

    user.email_user(subject, message)
