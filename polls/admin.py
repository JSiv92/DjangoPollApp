from django.contrib import admin

from .models import Choice, Question

# allow choices to be set when adding question inb admin ui
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    
    list_display = ('question_text', 'pub_date', 'was_published_recently') #columns to show
    list_filter = ['pub_date'] #filter by pub date
    search_fields = ['question_text'] #add search box to Question admin page

admin.site.register(Question, QuestionAdmin) # register to admin ui

