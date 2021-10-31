from django.shortcuts import render
from django.http import HttpResponse
from .models import Debate, CalculatedScore
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def debate_details(request):
    
    if request.user.groups.first().name == 'teams':
        username = request.user.username
        qry = Debate.objects.filter(team=username).order_by('-dnum')
        if qry.exists():
            query = qry[0]
            res_dict = {'debate':query, 'avail':True}
        else:
            res_dict = {'debate': 'Details currently unavailable', 'avail':False}
        return render(request, 'debateDetails.html', context=res_dict)
    else:
        return render(request, '400.html')

@login_required
def scores(request):
    if request.user.groups.first().name == 'admins':
        scoreslist = CalculatedScore.objects.all().order_by('dnum')
        res_dict = {'scores':scoreslist}
        return render(request, 'scores.html', context=res_dict)
    else:
        return render(request, '403.html')