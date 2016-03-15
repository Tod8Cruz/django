from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

# Create your views here.


def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'elections/index.html', context)


def areas(request, area):
    candidates = Candidate.objects.filter(area = '미국')
    context = {'candidates': candidates, 'area': area}
    return render(request, 'elections/area.html', context)
