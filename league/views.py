from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Teams, Results
from .forms import ResultForm
from .standings import calculate_table

# Create your views here.

def home(request):
    standings = calculate_table()
    return render(request, "league/index.html", {'standings': standings})

def teams(request):
    teams = Teams.objects.all() 
    return render(request, "league/teams.html", {'teams': teams})

@require_http_methods(["POST"])
def add_team(request):
    title = request.POST["title"]
    if len(title) > 0:
        team = Teams(title=title)
        team.save()

    return redirect("teams")

def delete_team(request, team_id):
    pass

def results(request):
    count = Teams.objects.all().count()
    count = (count - 1) * 2
    rounds = 'a' * count

    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = ResultForm()    

    return render(request, "league/results.html", {'rounds': rounds, 'form': form})


def show_round(request, round_id):
    matches = Results.objects.filter(round=round_id)
    return render(request, "league/round.html", {'matches': matches, 'round': round_id})
