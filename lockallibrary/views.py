from django.shortcuts import render


def home(request):
    text = 'home page'
    context = {'text': text}
    return render(request, 'home.html', context)
