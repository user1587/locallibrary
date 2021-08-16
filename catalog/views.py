from django.shortcuts import render


# Create your views here.
def home(request):
    text = 'catalog'
    context = {'text': text}
    return render(request, 'catalog/home.html', context)
