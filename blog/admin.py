from django.contrib import admin
from blog.models import Author, Tag, Posts, Comments
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)


class PostsAdmin(admin.ModelAdmin):
    list_filter = ("tags", "author", "date", )
    list_display = ("title", "excerpt", "date")
    prepopulated_fields = {"slug": ("title",)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "text", "post")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)
