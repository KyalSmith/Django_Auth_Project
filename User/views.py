from django.shortcuts import render
from .forms import UserProfileInfoForm,UserForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse



def index(request):

    return render(request,'index.html')


# Create your views here.
def user_login(request):

    Logged_In = False
    Bad_User = False

    if request.method == "POST":


        username = request.POST['username']
        password = request.POST['password']
        print(request)

        user = authenticate(request,username=username,password=password)

        if user is not None:



            if user.is_authenticated:

                Logged_In=True

                login(request,user)



        else:
            Bad_User = True
            print("Bad Login:\t {}\t:\t{}".format(username,password))





    return render(request,'login.html',{'Logged_In':Logged_In,'Bad_User':Bad_User})





def register(request):

    registered = False

    if request.method == "POST":

        userprofile_form = UserProfileInfoForm(data=request.POST)
        user_form = UserForm(data=request.POST)

        if userprofile_form.is_valid() and user_form.is_valid():

            print(user_form.data)
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile_data =userprofile_form.save(commit=False)
            profile_data.username = user
            print(userprofile_form.data)
            print(userprofile_form.data['username'])

            if 'profile_pic' in request.FILES:

                profile_data.picture = request.FILES('profile_pic')



            profile_data.save()

            registered=True

            return render(request, 'registration.html', {'user_form': user_form, 'profile_form': userprofile_form, 'registered': registered})

        else:
            print(user_form.errors)
            print(userprofile_form.errors)

    else:



        user_form = UserForm()
        profile_form = UserProfileInfoForm()


        return render(request,'registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))