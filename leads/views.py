
from django.shortcuts import render,redirect
from . models import Lead,Agent
from . forms import LeadModelForm


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/leads/all")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request, "registeration/register.html", {"form": form})

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, "registeration/login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')



def landing_page(request):
    return render(request,"landing.html")


def lead_list(request):
    leads=Lead.objects.all()
    return render(request,'leads/lead_list.html',{'lead_data':leads})

def lead_detail(request,pk):
    print(pk)
    lead=Lead.objects.get(id=pk)
    print('\n\n **************** ',lead)
    return render(request, 'leads/lead_detail.html', {'lead_data': lead})

def lead_create(request):
    form=LeadModelForm()
    if request.method=="POST":
        print('recived data')
        form=LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            # Since we are using ModelForm instead of Form, we don't type to type all these things
            # Just need to do form.save()

            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = Agent.objects.first()
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent
            # )


            return redirect("/leads/all")

    return render(request,'leads/lead_create.html',{"forms":form})

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads/all")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads/all")


