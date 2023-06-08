from django.contrib import admin
from newspaper.models import Newsletter, Post, Category, Tag, Contact, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Newsletter)