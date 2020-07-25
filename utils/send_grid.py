import requests
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class SendGridEmailBackend(BaseEmailBackend):
    def send_email(self, to_email, email_subject, email_body):
        url = 'https://api.sendgrid.com/v3/mail/send'

        email_body = email_body.replace('\n', '<br />')

        payload = '''
                  {
                      "personalizations": [
                      {
                          "to": [
                              {
                                  "email": "to_email"
                              }
                          ],
                          "subject": "email_subject"
                      }
                    ],
                      "from": {
                          "email": "from_email"
                      },
                      "content": [
                          {
                              "type": "text/html",
                              "value": "email_body"
                          }
                      ]
                  }'''.replace('to_email', to_email)\
                      .replace('email_subject', email_subject)\
                      .replace('from_email', settings.DEFAULT_FROM_EMAIL)\
                      .replace('email_body', email_body)

        headers = {
            'Authorization': f'Bearer {settings.SENDGRID_API_KEY}',
            'Content-Type': 'application/json'
        }

        response = requests.request('POST', url, headers=headers, data=payload)
        if response.status_code != 202:
            raise Exception(f'{payload}\n{response.status_code}\n{response.content}')

    def send_messages(self, email_messages):
        for email_message in email_messages:
            self.send_email(email_message.to[0], email_message.subject, email_message.body)
