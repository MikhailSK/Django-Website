from django.contrib import admin

from .models import Option, Riddle, Question, Choice

admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Question)
admin.site.register(Choice)