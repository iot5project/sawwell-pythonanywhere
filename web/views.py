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

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):

        id = request.POST['id'];
        pwd = request.POST['pwd'];
        context = {};
        try:
            cust = Cust.objects.get(id=id);
            if cust.pwd == pwd:
                request.session['sessionid'] = cust.id;
                request.session['sessionname'] = cust.name;
            else:
                raise Exception;
        except:
            print("login fail")
        return render(request, 'home.html', context);

    @request_mapping('/register')
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        add = request.POST['add'];
        email = request.POST['email'];
        print(id, pwd, name, add, email);
        context = {};
        try:
            Cust.objects.get(id=id);
        except:
            Cust(id=id, pwd=pwd, name=name, add=add, email=email).save();
            print("register fail")
        return render(request, 'home.html');

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



