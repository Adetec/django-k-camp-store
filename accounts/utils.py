from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .tokens import ConfirmEmailTokenGenerator


confirm_email_token_generator = ConfirmEmailTokenGenerator()

def send_confirmation_email(request, user):
    token = confirm_email_token_generator.make_token(user)
    domain = str(get_current_site(request))

    subject = 'Activate your account'
    message = render_to_string(
        'registration/account-activation-email.html',
        {
            'user': user,
            'token': token,
            'domain': domain
        }
    )

    user.email_user(subject, message)
