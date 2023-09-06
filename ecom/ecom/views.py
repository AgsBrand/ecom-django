from django.shortcuts import render


# defining home view 
def home(request):
    return render(request, 'home.html')


def new_arrival(request):
    return render(request, 'new-arrival.html')