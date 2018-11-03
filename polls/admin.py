from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text', 'pub_date',]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        ('Question information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)