from django.utils.crypto import get_random_string

def get_email_verification_token() :
	return get_random_string(32)


