from django.shortcuts import render

# Create your views here.

from .models import Dancer, Coach


def index(request):
    num_dancers = Dancer.objects.all().count()
    num_coaches = Coach.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_players': num_dancers, 'num_teams': num_coaches, 'num_visits': num_visits},
    )


from django.views import generic


class DancerListView(generic.ListView):
    model = Dancer
    paginate_by = 3


class DancerDetailView(generic.DetailView):
    model = Dancer


class CoachListView(generic.ListView):
    model = Coach
    paginate_by = 3


class CoachDetailView(generic.DetailView):
    model = Coach