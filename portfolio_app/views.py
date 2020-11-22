from django.shortcuts import render
from .models import Portfolio

def index(request):
    portfolio_projects = Portfolio.objects.all().order_by("-pk")
    return render(request,'portfolio_app/home.html', {'portfolio_projects':portfolio_projects})