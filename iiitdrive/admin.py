from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	list_filter = ('is_admin', 'is_active')
	list_display = ('username', 'date_joined', 'is_admin')
	filter_horizontal = ()

	fieldsets = (
		(None, {'fields': ('uid', 'username', 'email', 'password')}),
		('Verification', {'fields': ('email_verified', 'email_verification_token')}),
		('Permissions', {'fields': ('is_active', 'is_admin')}),
		('Important Dates', {'fields': ('date_joined', 'last_login')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'password1', 'password2'),
		}),
	)

	readonly_fields_list = ('uid', 'date_joined', 'email', 'email_verification_token')
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return self.readonly_fields_list
		else:
			return ()

	search_fields = ('username',)
	ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
