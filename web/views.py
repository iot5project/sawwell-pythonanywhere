from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust, Seocho


@request_mapping('')
class MyView(View):

    @request_mapping('/')
    def home(self, request):
        return render(request, 'home.html')

    @request_mapping('/login')
    def login(self, request):
        return render(request, 'logins.html')

    @request_mapping('/logout')
    def logout(self, request):
        if request.session['sessionid'] is not None:
            del request.session['sessionid']
        return render(request, 'home.html')

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        id = request.POST['id']
        password = request.POST['password']
        context = {}
        try:
            cust = Cust.objects.get(id=id)
            if cust.password == password:
                data = Cust.objects.get(id=id)
                request.session['sessionid'] = id
                html = 'home.html'
            else:
                raise Exception
        except:
            print("login fail")
            html = 'logins.html'
        return render(request, html, context)

    @request_mapping("/idfind", method="get")
    def idfind(self, request):
        email = request.GET.get('email', False)
        try:
            cust = Cust.objects.get(email=email)
            if cust.email == email:
                print("idokokok")
            else:
                raise Exception
        except:
             print("idnonono")
        return render(request, 'idFind.html')

    @request_mapping("/pwdfind", method="get")
    def pwdfind(self, request):
        id = request.GET.get('id', False)
        email = request.GET.get('email', False)
        try:
            cust = Cust.objects.filter(email=email, id=id)
            print("pwdokokok")
            if cust.count() == 0:
                print("pwdnonono")
        except:
            print("")
        return render(request, 'pwdFind.html')

    @request_mapping('/register')
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        print(id, password, name, address, email)
        context = {}
        try:
            Cust.objects.get(id=id)
            print("register fail")
        except:
            Cust(id=id, password=password, name=name, address=address, email=email).save()
            print("register ok")
        return render(request, 'home.html', context)

    @request_mapping('/korean')
    def korean(self, request):
        return render(request, 'market/koreanfood.html')

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

    @request_mapping('/menu')
    def menu(self, request):
        return render(request, 'menu.html')

    @request_mapping('/chart11')
    def chart11(self, request):
        return render(request, 'chart11.html')

    @request_mapping("/seocho", method="get")
    def all(self, request):
        page = request.GET.get('page', '1')
        market_list = Seocho.objects.order_by('marketno')
        paginator = Paginator(market_list, 9)
        page_obj = paginator.get_page(page)
        print(page_obj.query)
        context = {
            'center': 'seocho.html',
            'objs': page_obj
        }
        return render(request, 'seocho.html', context)
