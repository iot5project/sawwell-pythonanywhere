from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


class MarketView(View):

    @request_mapping('/korean')
    def login(self, request):
        return render(request, 'koreanfood.html')

    @request_mapping('/chicken')
    def login(self, request):
        return render(request, 'chicken.html')

    @request_mapping('/deseert')
    def login(self, request):
        return render(request, 'deseert.html')

    @request_mapping('/fastfood')
    def login(self, request):
        return render(request, 'fastfood.html')

    @request_mapping('/japan')
    def login(self, request):
        return render(request, 'japan.html')

    @request_mapping('/pizza')
    def login(self, request):
        return render(request, 'pizza.html')

    @request_mapping('/westernfood')
    def login(self, request):
        return render(request, 'westernfood.html')

    @request_mapping('/japan')
    def login(self, request):
        return render(request, 'japan.html')

    @request_mapping('/japan')
    def login(self, request):
        return render(request, 'japan.html')

    @request_mapping('/japan')
    def login(self, request):
        return render(request, 'japan.html')