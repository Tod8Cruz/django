from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Candidate, Poll, Choice
import datetime

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'elections/index.html', context)


def areas(request, area):
    today = datetime.datetime.now()
    poll = Poll.objects.get( start_date__lte = today, end_date__gte = today)
    if poll:
        candidates = Candidate.objects.filter(area = area)
        context = {'candidates': candidates, 
        'area': area,
        'poll_id': poll.id}
    else:
        context = {'no_poll': True, 'area': area}
    return render(request, 'elections/area.html', context)


def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice']
    choice = Choice.objects.get(poll_id = poll_id, candidate_id = selection)
    if choice:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('elections:result',args=(poll_id,)))
    else:
        choice = Choice()


def result(request, poll_id):
    return HttpResponse("result")