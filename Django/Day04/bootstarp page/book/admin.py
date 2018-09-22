from django.contrib import admin

# Register your models here.
from book.models import Book

# admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):

    #列表页面的属性
    list_display = ['title','publish_date'] #显示的字段
    search_fields = ['title'] #搜索字段
    list_filter = ['publish_date'] #过滤器
    date_hierarchy = 'publish_date' #水平时间筛选没有列表框
    ordering = ['-publish_date'] #-降顺序 + 升序
    list_per_page = 2 #每页显示数量
    # actions_on_top = False #不显示顶部动作
    # actions_on_bottom = True #显示底部动作

    #添加，修改页面
    # fields = ['title', 'publish_date', 'author', 'publishers'] #需要按顺序显示的字段
    # exclude = ['title']
    # filter_horizontal = ['publishers'] #用于多对多关系
    # filter_vertical = ['publishers']
    # raw_id_fields = ['author']
    fieldsets = ( ('书籍信息',{'fields':('title','publish_date')}),
                  ('出版社信息',{'fields':('publishers',)}))
admin.site.register(Book,BookAdmin)