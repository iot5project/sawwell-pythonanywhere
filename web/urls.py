from django_request_mapping import UrlPattern

from web.views import MyView
from web.views_market import MarketView


urlpatterns = UrlPattern()
urlpatterns.register(MyView)
urlpatterns.register(MarketView)
