from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping('')
class MyView(View):

    @request_mapping('/')
    def home(self, request):
        return render(request, 'home.html')

    @request_mapping('/login')
    def login(self, request):
        return render(request, 'logins.html')

    @request_mapping('/register')
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping('/korean')
    def korean(self, request):
        return render(request, 'market/koreanfood.html')

    @request_mapping('/chicken')
    def chicken(self, request):
        return render(request, 'market/chicken.html')

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


