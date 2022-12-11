from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

import uuid

from .utils import get_email_verification_token

@deconstructible
class AllowlistEmailValidator(EmailValidator):
# https://stackoverflow.com/a/61854214/12512406
    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, AllowlistEmailValidator) and super().__eq__(other)

#https://stackoverflow.com/a/58495709/12512406
class LowercaseEmailField(models.EmailField):
	def to_python(self, value):
		value = super(LowercaseEmailField, self).to_python(value)
		if isinstance(value, str):
			return value.lower()
		return value



class CustomUserManager(BaseUserManager):
	def create_user(self, email, username, password = None, is_active = False, is_admin = False):
		user = self.model(email = self.normalize_email(email), username = username, is_active = is_active, is_admin = is_admin)

		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, username, password = None):
		return self.create_user(email = email, username = username, password = password, is_active = True, is_admin = True)

class CustomUser(AbstractBaseUser):
	uid = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
	email = LowercaseEmailField(verbose_name = 'Email address', help_text = 'only IIITD emails', unique = True, max_length = 50, validators = [AllowlistEmailValidator(allowlist=['iiitd.ac.in']), ])
	username = models.CharField(unique = True, max_length = 30, blank = False)

	email_verified = models.BooleanField(verbose_name = 'Email Verified?', default = False)
	email_verification_token = models.CharField(unique = True, max_length = 32, default = get_email_verification_token)

	date_joined = models.DateTimeField(auto_now_add = True)

	is_active = models.BooleanField(verbose_name = 'Is Active?', default = False)
	is_admin = models.BooleanField(verbose_name = 'Is Admin?', default = False)

	objects = CustomUserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ('email', )

	def __str__(self):
		return f'{self.username}'

	def has_perm(self, perm, obj = None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin

	@property
	def is_superuser(self):
		return self.is_admin
