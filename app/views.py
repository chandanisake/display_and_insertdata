from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
   
def display_accessrecord(request):
    QSARO=AccessRecord.objects.all()
    d={'QSARO':QSARO}

    return render(request,'display_accessrecord.html',d)



def insert_topic(request):#1 htmlpage to 2 views
    topicname=input('enter topicname')
    TO=Topic.objects.get_or_create(topicname=topicname)[0]
    TO.save()

    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)



def insert_webpage(request):
    tn=input('enter topicname:')
    na=input('enter name:')
    ur=input('enter url:')

    TO=Topic.objects.get(topicname=tn)
    
    WO=Webpage.objects.get_or_create(topicname=TO,name=na,url=ur)[0]
    WO.save()
  
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)





def insert_accessrecord(request):
    pk=input('enter pk:')
    da=input('enter date:')
    au=input('enter author:')

    WO=Webpage.objects.get(pk=pk)
   
    AO=AccessRecord.objects.get_or_create(pk=pk,date=da,author=au)[0]
    AO.save()

    QSARO=AccessRecord.objects.all()
    d={'QSARO':QSARO}
    return render(request,'display_accessrecord.html',d)
    











   




   



