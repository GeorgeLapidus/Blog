from django.shortcuts import render

# Create your views here.
from main.models import Category


def start_page(request):
    categories = Category.objects.all()

    context = {'categories':categories}

    return render(request, 'start_page.html', context)