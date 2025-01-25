from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        return HttpResponse("Сообщение отправлено")
    else:
        return render(request, 'contacts.html')




