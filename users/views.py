from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # current_user = request.user
        # user_name = current_user.username
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error, please try again...~..~"))
            return redirect('adminlogin')
    else:
        return render(request, 'adminlogin.html', {})

def logout_admin(request):
    logout(request)
    return redirect('index')
