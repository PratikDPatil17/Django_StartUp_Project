from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.
def register(request):
    if request.method == 'POST':
        # print("Submitted REG")
        # return redirect ('register')
        # Register User 
        # messages.error (request, 'Testing error message')
        # return redirect ('register')
        
        # Get form values 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Check if password match
        if password == password2:
            # check user name
            # default user model
            if User.objects.filter ( username = username).exists():
                messages.error(request, 'That Username is taken')
                return redirect ('register')
            else :
                if User.objects.filter ( email = email).exists():
                    messages.error(request, 'That Email is taken')
                    return redirect ('register')
                else:
                    user = User.objects.create_user (username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                    # auth.login (request, user)
                    # messages.success (request, 'You are now logged in ')
                    # return redirect ('index')
                    user.save()
                    messages.success(request, 'You are now registered an can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Password do not match')
            return redirect ('register')

    else:
        return render (request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # return redirect ('login')
        # login User 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect ('login')

    else:
        return render (request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are Logged Out')
        return redirect ('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    context = {
        'contacts' : user_contacts
    }
    return render (request, 'accounts/dashboard.html', context)