from django.shortcuts import render,redirect
import random
from core.models import User
# Create your views here.


def index(request):
    return render(request, "core/index.html")


def signup(request):
    
    users = User.objects.all()
    if request.method == 'POST':
        u_name = request.POST['username']
        u_email = request.POST['email']
        u_date = request.POST['age']
        u_password = request.POST['password']
        User.objects.create(
            name = u_name,
            email = u_email,
            date = u_date,
            password = u_password,
        )
        return redirect('main')
        return render(request, "core/sign_up.html")
    return render(request, "core/sign_up.html")



def magic(request):
    if request.method == 'POST':
        user_number = int(request.POST["user_guess"])
        random_number = random.randint(0,100)
        if user_number == random_number:
            result = 'You guessed the number!'
        else:
            result = f'You failed =( The number was: {random_number}'
        return render(request, "core/magic.html",{'result': result})
    return render(request, "core/magic.html")
