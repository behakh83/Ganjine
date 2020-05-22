from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.admin import GenericTabularInline
from rest_framework.authtoken.models import Token
from api.models import Collection, Question


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class CollectionAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Question)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Token)

