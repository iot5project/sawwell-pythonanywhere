from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping('/review')
class ReviewView(View):

    @request_mapping('/reviewlist')
    def reviewlist(self, request):
        return render(request, 'review/list.html')



