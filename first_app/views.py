from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.

def index(request):
    weblist = AccessRecord.objects.order_by('date')
    date_dic = {'access_records': weblist}
    return render(request, 'first_app/index.html', context=date_dic)

def hello(request):
    hello_dic = {'insert_hello': 'hello world'}
    return render(request, 'first_app/hello.html', context=hello_dic)

def show_form(request):
    form = forms.FormName()
    return render(request, 'first_app/form.html', {'form': form})
