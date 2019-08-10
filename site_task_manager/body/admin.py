from django.contrib import admin

from .models import Option, Riddle, Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Choice)