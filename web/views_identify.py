from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping
from web.models import Cust


@request_mapping('/identify')
class IdentifyView(View):

    @request_mapping('/login')
    def login(self, request):
        return render(request, 'identify/logins.html')

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
            html = 'identify/logins.html'
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
        return render(request, 'identify/idFind.html')

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
        return render(request, 'identify/pwdFind.html')

    @request_mapping('/register')
    def register(self, request):
        return render(request, 'identify/register.html')

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
