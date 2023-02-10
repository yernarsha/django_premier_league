from .models import Teams, Results

def calculate_table():
    standings = []

    teams = Teams.objects.all() 
    for team in teams:
        standings.append({'title': team.title, 'matches': 0, 'wins': 0, 'draws': 0, 'losses': 0,
                          'goalsfor': 0, 'goalsagainst': 0, 'goalsdiff': 0, 'points': 0})
        
    matches = Results.objects.all()
    for match in matches:
        home_team = match.home_team_id
        away_team = match.away_team_id
        home_goals = match.home_goals
        away_goals = match.away_goals

        di = standings[home_team-1]
        d2 = standings[away_team-1]
        di['matches'] += 1
        d2['matches'] += 1

        if home_goals > away_goals:
            di['wins'] += 1
            d2['losses'] += 1
            di['points'] += 3
            di['goalsfor'] += home_goals
            d2['goalsfor'] += away_goals
            di['goalsagainst'] += away_goals
            d2['goalsagainst'] += home_goals
            di['goalsdiff'] = di['goalsfor'] - di['goalsagainst']
            d2['goalsdiff'] = d2['goalsfor'] - d2['goalsagainst']
        elif home_goals < away_goals:
            di['losses'] += 1
            d2['wins'] += 1
            d2['points'] += 3
            di['goalsfor'] += home_goals
            d2['goalsfor'] += away_goals
            di['goalsagainst'] += away_goals
            d2['goalsagainst'] += home_goals
            di['goalsdiff'] = di['goalsfor'] - di['goalsagainst']
            d2['goalsdiff'] = d2['goalsfor'] - d2['goalsagainst']
        else:
            di['draws'] += 1
            d2['draws'] += 1
            di['points'] += 1
            d2['points'] += 1
            di['goalsfor'] += home_goals
            d2['goalsfor'] += home_goals
            di['goalsagainst'] += home_goals
            d2['goalsagainst'] += home_goals

        standings[home_team-1] = di
        standings[away_team-1] = d2

    standings = sorted(standings, key=lambda x: x["points"], reverse=True)    

    return standings