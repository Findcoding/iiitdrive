
from django.conf import settings
from django.utils.crypto import get_random_string
from django.core.mail import send_mail, EmailMessage

import threading


def get_email_verification_token() :
	return get_random_string(32)


# Reference: https://stackoverflow.com/a/32980725/12512406
class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, sender):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
        msg.content_subtype = 'html'
        msg.send()

def send_email(subject, to_email, message):
    if type(to_email) != [list, tuple] :
        to_email = [to_email, ]
    from_email = settings.EMAIL_HOST_USER
    EmailThread(subject, message, to_email, from_email).start()
