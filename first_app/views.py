from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(request):
    weblist = AccessRecord.objects.order_by('date')
    date_dic = {'access_records': weblist}
    return render(request, 'first_app/index.html', context=date_dic)
