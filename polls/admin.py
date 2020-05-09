from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extrta = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('시간정보',  {'fields': ['pub_date']}),

    ]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]  # ChoiceInline이 상단에 선언되어 있어야함


admin.site.register(Question, QuestionAdmin)

