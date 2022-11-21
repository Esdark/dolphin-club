from django.contrib import admin
from .models import AgeMaster,MaterialMaster,ProductMaster,ProductAgeWiseList
# Register your models here.
# from .models import (GalleryPageMaster)


# class GallerymasterAdmin(admin.ModelAdmin):
#     fields  = ('Description', 'display', 'displayorder','upload')
#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         obj.save()
class AgemasterAdmin(admin.ModelAdmin):
    fields  = ('description', 'position', 'hide')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class MaterialmasterAdmin(admin.ModelAdmin):
    fields  = ('materialname', 'position', 'hide')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class ProductmasterAdmin(admin.ModelAdmin):
    fields  = ('productid','name','Description','material','position', 'hide','productimage')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    

class ProductAgemasterAdmin(admin.ModelAdmin):
    fields  = ('productid','age','position','stock','hide')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(AgeMaster,AgemasterAdmin)
admin.site.register(MaterialMaster,MaterialmasterAdmin)
admin.site.register(ProductMaster,ProductmasterAdmin)
admin.site.register(ProductAgeWiseList,ProductAgemasterAdmin)

admin.site.site_header = "Dolphin Admin"
admin.site.site_title = "Dolphin Admin Page"
admin.site.index_title = "Welcome to Dolphin Page Manager"
