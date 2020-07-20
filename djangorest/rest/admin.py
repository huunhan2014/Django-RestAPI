from django.contrib import admin
from .models import Post, Type, Product, FieldPlanningRun

# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'draft', 'updated', 'created')
    list_filter = ['created', 'updated']
    search_fields = ['title']

class TypeModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('name', 'active', )

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name','type_id', 'price', 'quantity', 'description')
    list_filter = ('type_id',)

admin.site.register(Post, PostsAdmin)
admin.site.register(Type, TypeModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(FieldPlanningRun)

