from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.admin import GenericTabularInline
from rest_framework.authtoken.models import Token
from api.models import Collection, Question


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    show_change_link = True


class CollectionAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('static/css/custom_admin_panel.css',)
        }
    inlines = [
        QuestionInline,
    ]


class QuestionAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('static/css/custom_admin_panel.css',)
        }


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Token)

