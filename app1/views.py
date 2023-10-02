from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from multiprocessing import context


# Create your views here.

def Home(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        return redirect('showdata')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def Delete_record(id):
    a = Employee.objects.get(pk=id)
    a.delete()
    return redirect('showdata')


def Update_record(request, id):
    if request.method == 'POST':
        data = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('showdata')

    else:
        data = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=data)

    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


def Showdata(request):
    # form = EmployeeForm(request.POST)
    data = Employee.objects.all()

    context = {
        # 'form': form,
        'data': data,
    }
    return render(request, 'showdata.html', context)
