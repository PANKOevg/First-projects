from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CmsSlider


class CmsAdm(admin.ModelAdmin):
    #Настройка админки для Слайдов
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)


    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="150px"')
        else:
            print("Картинка не найдена")

    get_img.short_description = 'Слайд'


admin.site.register(CmsSlider, CmsAdm)
