from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Review, Reply, Cust, Market


@request_mapping('/review')
class ReviewView(View):

    @request_mapping('/reviewlist')
    def reviewlist(self, request):
        obj = Cust.objects.all()
        objects = Market.objects.all()
        context = {
            'objs': obj,
            'objects': objects
        }
        return render(request,'review/list.html',context);

    @request_mapping("/reviewimpl", method="post")
    def reviewimpl(self, request):
        star = request.POST['star'];
        content = request.POST['content'];
        print(star, content);
        context = {};
        Review(content=content, star=star).save();
        print("register ok")
        return render(request, 'review/list.html', context);

    @request_mapping("/replyimpl", method="post")
    def replyimpl(self, request):
        content = request.POST['reply'];
        print(content);
        context = {};
        Reply(content=content).save();
        print("register ok")
        return render(request, 'review/list.html', context);
