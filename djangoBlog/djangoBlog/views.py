from django.shortcuts import render ,HttpResponse

def about(request):
    # return HttpResponse('hi there, im sevda!')
    return render(request, 'about.html')


def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')


