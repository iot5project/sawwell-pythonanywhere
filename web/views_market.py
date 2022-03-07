from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping('/market')
class MarketView(View):

    @request_mapping('/korea')
    def korea(self, request):
        return render(request, 'koreanfood.html')