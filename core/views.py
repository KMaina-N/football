from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import FootballTeam
import json

# Create your views here.
def index(request):
    context = {}
    football_team = FootballTeam.objects.all()
    context['football'] = football_team
    return render(request, 'index.html', context)
# def index(request):
#     football = FootballTeam.objects.all()
#     football = json.loads(football)
#     return JsonResponse(football)

def add_team(request):
    if request.method == 'POST':
        team = request.POST.get('team_name')
        city = request.POST.get('team_city')
        win = request.POST.get('win')
        if win == None:
            win = False
        print('team: ', team)
        print('city: ', city)
        print('win: ', win)
        FootballTeam.objects.create(team_name=team, team_city=city, win=win)
        return redirect('index')
    return render(request, 'add.html')

def delete_team(request, pk):
    team = FootballTeam.objects.get(id=pk)
    team.delete()
    return redirect('index')


def edit_team(request, pk):
    if request.method == 'POST':
        team = request.POST.get('team_name')
        city = request.POST.get('team_city')
        win = request.POST.get('win') 

                    
        team_data = FootballTeam.objects.get(id=pk)
        if team == '':
            print(team_data.team_name)
            team = team_data.team_name
        if city == '':
            print('new city',team_data.team_city)
            city == team_data.team_city
        if win == None:
            win = False
        
        team_data.team_name = team
        team_data.team_city = city
        team_data.win = win
        team_data.save()
        return redirect('index')
    return render(request, 'add.html')
        
    