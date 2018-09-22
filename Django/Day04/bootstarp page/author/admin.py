from django.contrib import admin

# Register your models here.
from author.models import Author

# admin.site.register(Author)
#定制管理
class AuthorAdmin(admin.ModelAdmin):

    def show_gender(self):
        if self.gender:
            return '男'
        return '女'

    list_display = ['first_name','last_name','email',show_gender]
    show_gender.short_description = '性别'


admin.site.register(Author,AuthorAdmin)