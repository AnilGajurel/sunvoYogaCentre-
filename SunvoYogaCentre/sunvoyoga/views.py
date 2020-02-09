from django.shortcuts import render,redirect
from sunvoyoga.forms import UserForm,CustomerForm,BookingForm
from sunvoyoga.models import User,Customer,Booking
from django.http import HttpResponse,JsonResponse

from django.contrib import messages

from sunvoyoga.authenticate import Authenticate



def home(request):
    return render(request,"sunvoyoga/Home.html")

def classes(request):
    return render(request,"sunvoyoga/Classes.html")



def booking(request):
    if request.method == "POST":
        fname = request.POST['fname ']
        lname  = request.POST['lname ']
        email  = request.POST['email ']
        mobnumber  = request.POST['mobnumber ']
        classes  = request.POST['classes ']
        gender  = request.POST['gender  ']

        bookingdata = Booking(fname=fname, lname=lname, username=username, email=email,
                              mobnumber=mobnumber, classes=classes,gender=gender)
        bookingdata.save()
        print("Booked ")
        return redirect('/')

    else:
        return render(request, "sunvoyoga/booking.html")



def search(request):
    users=User.objects.filter(email__contains=request.GET['search']).values()
    return JsonResponse(list(users),safe=False)


#Admin signup
def create(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass


    form=UserForm()
    return render(request,"sunvoyoga/create.html",{'form':form})


def edit(request,id):
    user=User.objects.get(id=id)
    return render(request,"sunvoyoga/edit.html",{'user':user})

def update(request,id):
    user = User.objects.get(id=id)
    form=UserForm(request.POST,instance=user)
    form.save()
    return redirect("/")

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/")


def adminLogin(request):
    return render(request,"sunvoyoga/AdminLogin.html")

def adminLogOut(request):
    auth.logout(request)
    return render(request,"sunvoyoga/home.html")

def entry(request):
    request.session['email']=request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/dashboard')


@Authenticate.valid_user
def show(request):
    limit = 3
    page = 1
    if request.method == "POST":
        if "next" in request.POST:
            page = (int(request.POST['page']) + 1)
        elif "prev" in request.POST:
            page = (int(request.POST['page']) - 1)
        tempoffset = page - 1
        offset = tempoffset * page
        users = User.objects.raw("select * from user limit 2 offset %s", [offset])
    else:
        users = User.objects.raw("select * from user limit 2 offset 0")

    return render(request, "sunvoyoga/show.html", {'users': users, 'page': page})


#Sign up for customer
def signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname = request.POST['lname']
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password==repassword:
            if Customer.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('/signup')
            elif Customer.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('/signup')
            else:
                customerdata=Customer(fname=fname,lname=lname,username=username,email=email,
                                            password=password,repassword=repassword)
                customerdata.save()
                print("user created")
                return redirect('/')
        else:
            messages.info(request, "password not matching")
            return redirect('/signup')
        return redirect('/')
    else:
        return render(request,"sunvoyoga/signup.html")


#login for Customer
def login(request):
    return render(request,"sunvoyoga/login.html")

def entryCustomer(request):
        request.session['email']=request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('/booking')

'''@Authenticate.valid_customer
def booking(request):
    customer=Customer.objects.all()
    return render(request,"sunvoyoga/booking.html",{'Customer':customer})
'''
@Authenticate.valid_customer
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass


    form=BookingForm()
    return render(request,"sunvoyoga/booking.html",{'form':form})


def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('/home')


def showCustomer(request):
    limit=2
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page = (int(request.POST['page']) + 1)

        elif "prev" in request.POST:
            page = (int(request.POST['page'])-1)


        tempoffset=page-1
        offset = tempoffset* page
        customers = Customer.objects.raw("select * from customer limit 2 offset %s",[offset])

    else:
        customers = Customer.objects.raw("select * from customer limit 2 offset 0")
    return render(request,"sunvoyoga/showCustomer.html",{'customers':customers,'page':page})




@Authenticate.valid_user
def dashboard(request):
    return render(request,"sunvoyoga/dashboard.html")

