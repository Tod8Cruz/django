from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

# Create your views here.
def index(request):
	candidates = Candidate.objects.all()
	str = ''
	for candidate in candidates:
		str += "{} 기호{}번({})<BR>".format(candidate.name,
			candidate.party_number,
			candidate.area)
		str += candidate.introduction+"<P>"
	return HttpResponse(str)