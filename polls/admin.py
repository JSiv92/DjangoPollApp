from django.contrib import admin

from .models import Question, Choice

#split admin form for Question into categories with fieldsets 
# (give them their own headings like Date information)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)