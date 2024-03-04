from django.contrib import admin
from django.utils.safestring import mark_safe
from catalog.models import Product, Category, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","name", "price", "category", "image_show"]
    list_filter = ["category", ]
    search_fields = ["name", ]


    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None
    
    image_show.__name__=="Картинка"

admin.site.register(Category)
admin.site.register(Order)