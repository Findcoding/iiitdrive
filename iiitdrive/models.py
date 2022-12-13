from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

import uuid
import os

from .utils import get_email_verification_token
from .model_fields import LowercaseCharField, LowercaseEmailField, RestrictedFileField

# https://stackoverflow.com/a/61854214/12512406
@deconstructible
class AllowlistEmailValidator(EmailValidator):
	def validate_domain_part(self, domain_part):
		return False

	def __eq__(self, other):
		return isinstance(other, AllowlistEmailValidator) and super().__eq__(other)


def change_filename(instance, filename) :
	path = str(instance.user.uid)
	format = str(uuid.uuid4()) + '.' + filename.split('.')[-1]
	return os.path.join(path, format)


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

class UserDetails(models.Model) :
	user = models.OneToOneField(get_user_model(), related_name = 'details', on_delete = models.CASCADE, null = False, blank = False, editable = False)
	profile_picture = RestrictedFileField(upload_to = change_filename, null = True, blank = True, content_types = ['image/jpg', 'image/jpeg'], max_upload_size = 1 * 1024 * 1024)
	about_me = models.CharField(max_length = 200, default = '', blank = True)

	def __str__(self):
		return f'{self.user.username}'


@receiver(post_save, sender = get_user_model())
def create_user_profile(sender, instance, created, *args, **kwargs):
	if created:
		UserDetails.objects.get_or_create(user = instance)
	instance.details.save()
