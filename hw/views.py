from django.shortcuts import render

def hello_world(request):
    return render(request,'hw/index.html',context={})
