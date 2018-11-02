from django.contrib import admin
from blog.models import BlogsPost, Person

# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(BlogsPost, BlogsPostAdmin)
admin.site.register(Person, PersonAdmin)