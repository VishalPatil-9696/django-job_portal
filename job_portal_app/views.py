from django.shortcuts import render,redirect
from .models import jobModel,mechJobModel,civilJobModel
from .forms import jobForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# AUTHENTICATION CODE

def home(request):
    return render(request,'home.html')

def register(request):
    data = jobForm()
    if request.method == "POST":
        data = jobForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/index/')
    return render(request,'register.html',{'form':data})

@login_required(login_url='home')
def index(request):
    return render(request,'index.html')

# IT JOBS CODE


def add(request):
    if request.method == "POST":
        Company_Name = request.POST['name']
        Position = request.POST['position']
        Package = request.POST['package']
        Experiance = request.POST['experiance']
        Opnnings = request.POST['opnnings']
        Location = request.POST['location']
        st = jobModel(Company_Name=Company_Name,Position=Position,Package=Package,Experiance=Experiance,Opnnings=Opnnings,Location=Location)
        st.save()
        return redirect('/read/')
    return render(request,'add.html')

def read(request):
    data = jobModel.objects.all()
    return render(request,'read.html',{'form':data})

def update(request,id):
    data = jobModel.objects.get(pk = id)
    if request.method == "POST":
        data.Company_Name = request.POST['name']
        data.Position = request.POST['position']
        data.Package = request.POST['package']
        data.Experiance = request.POST['experiance']
        data.Opnnings = request.POST['opnnings']
        data.Location = request.POST['location']
        data.save()
        return redirect('/read/')
    return render(request,'update.html',{'form':data})

def delete(request,id):
    data = jobModel.objects.get(pk = id)
    data.delete()
    return redirect('/read/')

# MECH JOB CODE

def read_mech(request):
    form = mechJobModel.objects.all()
    return render(request,'read_mech.html',{'form':form})

def add_mech(request):
    if request.method == "POST":
        Company_Name = request.POST['name']
        Position = request.POST['position']
        Package = request.POST['package']
        Experiance = request.POST['experiance']
        Opnnings = request.POST['opnnings']
        Location = request.POST['location']
        st = mechJobModel(Company_Name=Company_Name,Position=Position,Package=Package,Experiance=Experiance,Opnnings=Opnnings,Location=Location)
        st.save()
        return redirect('/read_mech/')
    return render(request,'add_mech.html')

def update_mech(request,id):
    form = mechJobModel.objects.get(pk = id)
    if request.method == "POST":
        form.Company_Name = request.POST['name']
        form.Position = request.POST['position']
        form.Package = request.POST['package']
        form.Experiance = request.POST['experiance']
        form.Opnnings = request.POST['opnnings']
        form.Location = request.POST['location']
        form.save()
        return redirect('/read_mech/')
    return render(request,'update_mech.html',{'form':form})

def delete_mech(request,id):
    form = mechJobModel.objects.get(pk = id)
    form.delete()
    return redirect('/read_mech/')

def read_civil(request):
    form = civilJobModel.objects.all()
    return render(request,'read_civil.html',{'form':form})

def add_civil(request):
    if request.method == 'POST':
        Company_Name = request.POST['name']
        Position = request.POST['position']
        Package = request.POST['package']
        Experiance = request.POST['experiance']
        Opnnings = request.POST['opnnings']
        Location = request.POST['location']
        st = civilJobModel(Company_Name=Company_Name,Position=Position,Package=Package,Experiance=Experiance,Opnnings=Opnnings,Location=Location)
        st.save()
        return redirect('/read_civil/')
    return render(request,'add_civil.html')

def update_civil(request,id):
    form = civilJobModel.objects.get(pk=id)
    if request.method == "POST":
        form.Company_Name = request.POST['name']
        form.Position = request.POST['position']
        form.Package = request.POST['package']
        form.Experiance = request.POST['experiance']
        form.Opnnings = request.POST['opnnings']
        form.Location = request.POST['location']
        form.save()
        return redirect('/read_civil/')
    return render(request,'update_civil.html',{'form':form})

def delete_civil(request,id):
    form = civilJobModel.objects.get(pk=id)
    form.delete()
    return redirect('/read_civil/')