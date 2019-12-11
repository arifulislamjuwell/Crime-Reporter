from django import template
from authenticate.models import Profile
register = template.Library()

@register.filter(name='user_check')
def user_check(user):
    try:
        profile =Profile.objects.get(user=user)
        type_of=profile.type_of
        return (type_of)
    except Exception as e:
        return e