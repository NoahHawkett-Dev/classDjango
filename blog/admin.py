from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    
admin.site.register(Post, PostAdmin)
print("hello")