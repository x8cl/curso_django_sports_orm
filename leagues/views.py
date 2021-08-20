from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues" : League.objects.all(),
		"teams" : Team.objects.all(),
		"players" : Player.objects.all()
	}
	return render(request, "leagues/index.html", context)

def lvl1(request):
	names_for_16 = [
		"Alexander",
		"Wyatt"
	]
	
	context = {
		"baseball_leagues" : League.objects.filter(sport__contains="baseball"),
		"women_leagues" : League.objects.filter(name__contains="women"),
		"hockey_leagues" : League.objects.filter(sport__contains="hockey"),
		"not_football_leagues" : League.objects.exclude(sport__contains="football"),
		"conferences_leagues" : League.objects.filter(name__contains="conference"),
		"atlantic_leagues" : League.objects.filter(name__contains="atlantic"),
		"dallas_teams" : Team.objects.filter(location__contains="dallas"),
		"raptors_teams" : Team.objects.filter(team_name__contains="raptors"),
		"location_city_teams" : Team.objects.filter(location__contains="city"),
		"begin_t_teams" : Team.objects.filter(team_name__startswith="t"),
		"ordered_location_teams" : Team.objects.all().order_by("location"),
		"ordered_name_reverse_teams" : Team.objects.all().order_by("-team_name"),
		"lastname_cooper_player" : Player.objects.filter(last_name__contains="cooper"),
		"firstname_joshua_player" : Player.objects.filter(first_name__contains="joshua"),
		"lastname_cooper_not_joshua_player" : Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),	
		"firstname_alexander_wyatt_player" : Player.objects.all().filter(first_name__in=names_for_16)
	}
	return render(request, "leagues/lvl1.html", context)

def lvl2(request):
	context = {
		"atlantic_soccer_league_teams" : Team.objects.filter(league=League.objects.get(name="Atlantic Soccer Conference")),
		"boston_penguins_players" : Player.objects.filter(curr_team=Team.objects.get(location="Boston", team_name="Penguins")),
		"icbc_league_players" : Player.objects.filter(curr_team__in=Team.objects.filter(league=League.objects.get(name="International Collegiate Baseball Conference"))).order_by("curr_team__location", "curr_team__team_name", "first_name"),
		"acaf_league_lopez_player" : Player.objects.filter(curr_team__in=Team.objects.filter(league=League.objects.get(name="American Conference of Amateur Football"))).filter(last_name="Lopez").order_by("first_name"),
		"all_football_players" : Player.objects.filter(curr_team__in=Team.objects.filter(league__in=League.objects.filter(sport="Football"))).order_by("curr_team__location", "curr_team__team_name", "first_name"),
		"player_sophia_teams" : Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia")).order_by("location"),
		"player_sophia_leagues" : League.objects.filter(teams__in=Team.objects.filter(curr_players__in=Player.objects.filter(first_name="Sophia"))).order_by("name"),
		"flores_not_wr_team_players" : Player.objects.filter(last_name="Flores").exclude(curr_team=Team.objects.get(location="Washington", team_name="Roughriders")).order_by("first_name")
	}
	return render(request, "leagues/lvl2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")