from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import logging
import json

from models import Game
from models import Record
from form import CreateForm


logger = logging.getLogger('django')


def create_view(request):
    logger.debug('enter create view')
    if request.method == 'POST':
        logger.debug('submit create post form')
        form = CreateForm(request.POST)
        if form.is_valid():
            game = Game(name=form.cleaned_data['name'],
                        circle=form.cleaned_data['circle'],
                        base=form.cleaned_data['base'],
                        member1=form.cleaned_data['member1'],
                        member2=form.cleaned_data['member2'],
                        member3=form.cleaned_data['member3'],
                        member4=form.cleaned_data['member4'])
            game.save()
            logger.debug('save game success')
            return HttpResponseRedirect('/record/list')
        else:
            logger.error('save game fail')
            return HttpResponseRedirect('/record/list')
    return render(request, 'record/create.html')


def list_view(request):
    logger.debug('enter list view')
    games = Game.objects.all()
    return render(request, 'record/list.html', {'games': games})


def record_view(request, game_id):
    logger.debug('enter record view')
    if request.method == 'POST':
        logger.debug('submit record post form')
        logger.debug(game_id)
        logger.debug(request.POST)
        record = Record(round=0,
                        score1=request.POST['score1'],
                        score2=request.POST['score2'],
                        score3=request.POST['score3'],
                        score4=request.POST['score4'])

        record.save()
        logger.debug('save record success')
        game = Game.objects.get(id=game_id)
        game.score1 += int(request.POST['score1'])
        game.score2 += int(request.POST['score2'])
        game.score3 += int(request.POST['score3'])
        game.score4 += int(request.POST['score4'])
        logger.debug(game)
        game.save()
        logger.debug('save game success')
    games = Game.objects.order_by('-start_dt')
    return render(request, 'record/record.html', {'games': games, 'game_id': game_id})


def show_view(request, gid):
    logger.debug('enter show view')
    game = Game.objects.get(id=gid)
    ret = {
        'name': game.name,
        'circle': game.circle,
        'base': game.base,
        'member1': game.member1,
        'member2': game.member2,
        'member3': game.member3,
        'member4': game.member4,
        'score1': game.score1,
        'score2': game.score1,
        'score3': game.score1,
        'score4': game.score1,
    }
    return HttpResponse(json.dumps(ret))
