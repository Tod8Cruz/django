from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate,Poll

import datetime

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'elections/index.html', context)


def areas(request, area):
    today = datetime.datetime.now()
    if Poll.objects.filter( start_date__lte = today, end_date__gte = today):
        candidates = Candidate.objects.filter(area = area)
        context = {'candidates': candidates, 'area': area}
    else:
        context = {'no_poll': True, 'area': area}
    return render(request, 'elections/area.html', context)
