from django.shortcuts import render ,HttpResponse

def about(request):
    return HttpResponse('hi there, im sevda!')


def home(request):
    return HttpResponse('home')