from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from elect.models import servicee,rev,contact

# Create your views here.
#create account page
def signuppage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("Your confirm password is not matching with the password")
        else:
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already taken")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already registered")
        
            else:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()
                return redirect('login')
    else:
        return render(request, 'signup.html')


#login view
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password!")
    return render(request, 'login.html')

#home page
def homepage(request):
    return render(request,'home.html')

#logout view
def logout_view(request):
    logout(request)
    return redirect('signup')

#bookings
def book(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        date = request.POST.get('date')
        service_type = request.POST.get('service_type')
        # Create and save a new ServiceRequest object
        if request.user.is_authenticated:
            service_request = servicee(
            user=request.user,
            name=name,
            email=email,
            phonenumber=phonenumber,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            date=date,
            service_type=service_type
            )
            service_request.save()
            return redirect('my_appointments')
        else:
            return redirect('login')
        
    return render(request,'bookings.html')

#to show the service we booked



def my_appointments(request):
    if request.user.is_authenticated:
        appointments = servicee.objects.filter(user=request.user)
        return render(request, 'appointments.html', {'appointments': appointments})
    else:
        return redirect('login')
    

    #to get reviews
def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')
        revs = rev(name=name, review=review)
        revs.save()
        return redirect('reviews')
    else:
        reviews = rev.objects.all()
        return render(request, 'home.html', {'reviews': reviews})
    
def cont(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        Contact=contact(name=name,email=email,phone=phone,subject=subject,message=message)
        Contact.save()
    return render(request,'home.html')

