from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
from web.models import Seocho


@request_mapping('/market')
class MarketView(View):

    @request_mapping('/chicken')
    def chicken(self, request):
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.order_by('marketno')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        context = {
            'objs': page_obj
        }
        return render(request, 'market/chicken.html', context)

    @request_mapping('/korea')
    def korea(self, request):
        return render(request, 'market/koreanfood.html')

    @request_mapping('/chinese')
    def chinese(self, request):
        return render(request, 'market/chinesefood.html')

    @request_mapping('/dessert')
    def dessert(self, request):
        return render(request, 'market/dessert.html')

    @request_mapping('/pizza')
    def pizza(self, request):
        return render(request, 'market/pizza.html')

    @request_mapping('/western')
    def western(self, request):
        return render(request, 'market/westernfood.html')

    @request_mapping('/fastfood')
    def fastfood(self, request):
        return render(request, 'market/fastfood.html')
