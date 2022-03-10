from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping
from webproject.web.models import Cust


@request_mapping('/identify')
class IdentifyView(View):

    @request_mapping('/login')
    def login(self, request):
        context = {
            'center': 'identify/logins.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/idfind")
    def idfind(self, request):
        context = {
            'center': 'identify/idFind.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping("/pwdfind")
    def pwdfind(self, request):
        context = {
            'center': 'identify/pwdFind.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/register')
    def register(self, request):
        context = {
            'center': 'identify/register.html'
        }
        return render(request, 'common/main.html', context)

    @request_mapping('/logout')
    def logout(self, request):
        if request.session['sessionid'] is not None:
            del request.session['sessionid']
        return render(request, 'common/home.html')

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
                html = 'common/home.html'
            else:
                raise Exception
        except:
            html = 'common/main.html'
            context['center'] = 'identify/logins.html'
        return render(request, html, context)

    @request_mapping("/idfindimpl", method="get")
    def idfindimpl(self, request):
        email = request.GET.get('email', False)
        context = {}
        try:
            cust = Cust.objects.get(email=email)
            if cust.email == email:
                print("idokokok")
                context = 'idFind.html'
            else:
                raise Exception
        except:
             print("idnonono")
        return render(request, 'identify/main.html', context)

    @request_mapping("/pwdfindimpl", method="get")
    def pwdfindimpl(self, request):
        id = request.GET.get('id', False)
        email = request.GET.get('email', False)
        try:
            cust = Cust.objects.filter(email=email, id=id)
            print("pwdokokok")
            if cust.count() == 0:
                print("pwdnonono")
        except:
            print("")
        return render(request, 'identify/pwdFind.html')

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
        return render(request, 'common/home.html', context)
