from django.shortcuts import render, redirect
from .forms import RecordForm
from django.contrib import messages
from .models import Records
from django.contrib.auth.decorators import login_required


def HomeView(request):
    return render(request, 'index.html')

@login_required
def RecordView(request):
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Missing Person Reported !")
            return redirect('/')
    else:
        form = RecordForm()
    
    context = {
        'form' : form
    }
    return render(request, 'record-form.html', context)

def LostPerson(request):
    context = {
        'record' : Records.objects.filter(status=False)
    }
    return render(request, 'lost-person.html', context)

def DetailView(request,pk):
    context = {
        'obj' : Records.objects.get(pk=pk)
    }
    return render(request, 'details.html', context)

@login_required
def MyEntries(request):
    context = {
        'record' : Records.objects.filter(current_user=request.user)
    }
    return render(request, 'my-entries.html', context)

def FoundPeople(request):
    context = {
        'record' : Records.objects.filter(status=True)
    }
    return render(request, 'found.html', context)

def DelReport(request,pk):
    record = Records.objects.get(pk=pk)
    record.delete()
    messages.success(request, 'Report Deleted Successfully')
    return redirect('/')

def ReportFound(request,pk):
    record = Records.objects.get(pk=pk)
    record.status = True
    record.save()
    messages.info(request,'Reported '+record.name+' found')
    return redirect('/')