from django.contrib import admin

from webproject.web.models import Categori


class Cust(admin.ModelAdmin):
    list_display = ('custno', 'id', 'password', 'name', 'address', 'email', 'regdate')


class CategoriAdmin(admin.ModelAdmin):
    list_display = ('cid', 'categoriname')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('foodid', 'name', 'price', 'regdate')


class MarketAdmin(admin.ModelAdmin):
    list_display = ('marketno', 'cid', 'foodid', 'marketname', 'marketaddress', 'regdate',
                    'open', 'close', 'holiday', 'hit')


class CeoAdmin(admin.ModelAdmin):
    list_display = ('ceoid', 'marketno', 'id', 'password', 'name')


class Reply(admin.ModelAdmin):
    list_display = ('replyno', 'reviewno', 'ceoid', 'content', 'regdate')


class Review(admin.ModelAdmin):
    list_display = ('', '')


admin.site.register(Categori,CategoriAdmin)
# Register your models here.
