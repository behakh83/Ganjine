from django.contrib import admin
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token

from api.models import Collection, Question

admin.site.register(Collection)
admin.site.register(Question)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Token)

