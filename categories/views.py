from django.shortcuts import render_to_response, redirect
from categories.models import Category


def categories(request):
    all_categories = Category.objects.all()
    return render_to_response('main.html', {'categories': all_categories})







