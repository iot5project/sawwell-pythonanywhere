from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping('')
class MyView(View):

    @request_mapping('/')
    def home(self, request):
        return render(request, 'home.html')

