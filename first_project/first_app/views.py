from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
from . import forms
from first_app.forms import NewUserForm

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,"first_app/index.html",context = date_dict)

def form_name_view(request):
    form = forms.FormName()


    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Successful")
            print("NAME:"+form.cleaned_data['name'])
            print("EMAIL:"+form.cleaned_data['email'])
            print("TEXT:"+form.cleaned_data['text'])

    return render(request,"first_app/form_page.html",{'form':form})

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
         form = NewUserForm(request.POST)
         if form.is_valid():
             form.save(commit = True)
             return index(request)
         else:
            print("Invalid form ERROR!")
    return render(request,'first_app/user.html',{'form':form})
