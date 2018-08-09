from django.contrib import admin
# from django.utils.text import Truncator

from .models import BlogType, Blog


# Register your models here.

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    # fields = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        # (None, {'fields': ['question_text']}),
        (None, {'fields': ('type_name', 'title', 'author',)}),
        ('内容', {'fields': ('content',)}),
        # ('时间', {'fields': ('create_time', 'last_update_time',)}),
    )

# admin.site.register(Blog)
