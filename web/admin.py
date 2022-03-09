from django.contrib import admin

from web.models import Categori, Cust, Ceo, Food, Market, Reply, Review, Seocho


class CustAdmin(admin.ModelAdmin):
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


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('replyid', 'reviewno', 'ceoid', 'content', 'regdate')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewno', 'marketno', 'custno', 'content', 'star', 'regdate')


class SeochoAdmin(admin.ModelAdmin):
    list_display = ('marketno', 'marketname', 'ceoname', 'address', 'phone', 'categori', 'food')


admin.site.register(Cust, CustAdmin)
admin.site.register(Categori, CategoriAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Ceo, CeoAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Seocho, SeochoAdmin)
