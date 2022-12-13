from django import template

register = template.Library()

@register.filter
def get_social_link(socials, name) :
	if socials.filter(name = name).exists():
		return socials.get(name = name).link
	else:
		return None
