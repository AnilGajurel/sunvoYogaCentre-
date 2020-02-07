from django.shortcuts import redirect
from sunvoyoga.models import User,Customer
from django.contrib import messages

class Authenticate:
    def valid_user(function):
        def wrap(request):
           # print(request.session['email'])
            try:

                User.objects.get(email=request.session['email'])
                User.objects.get(password=request.session['password'])
                return function(request)

            except:
                messages.warning(request,"Password or Email error")
                return redirect("/adminlogin")

        return wrap


    def valid_customer(function):
        def wrap(request):
           # print(request.session['email'])
            try:
                Customer.objects.get(email=request.session['email'])
                Customer.objects.get(password=request.session['password'])
                print(Customer.email)
                return function(request)

            except:
                messages.warning(request,"Password or Email error")
                return redirect("/login")

        return wrap

