from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import logging
import json
from django.forms.models import model_to_dict


from models import Game
from models import Record
from form import CreateForm


logger = logging.getLogger('django')


def dt2str(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def get_request_param(params):
    s_echo = params['sEcho']
    start = int(params['iDisplayStart'])
    length = int(params['iDisplayLength'])
    return s_echo, start, length


def delete_game_view(request):
    logger.debug("enter delete game view")
    game_id = request.POST['game_id']
    game = Game.objects.get(id=game_id)
    game.delete()
    ret = {
        'code': 200,
        'msg': 'delete success'
    }
    return HttpResponse(json.dumps(ret))


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


def list_json_view(request):
    logger.debug('enter list json view')
    logger.debug(request)
    s_echo, start, length = get_request_param(request.GET)
    games= []
    logger.debug(start)
    logger.debug(length)
    games_query = Game.objects.all()[start:start+length]
    logger.debug(len(games_query))
    for i in games_query:
        line = model_to_dict(i)
        line['start_dt'] = dt2str(i.start_dt)
        line['update_dt'] = dt2str(i.update_dt)
        games.append(line)
    ret = {
        'data': games,
        'sEcho': s_echo,
        'iTotalRecords': Game.objects.count(),
        'iTotalDisplayRecords': Game.objects.count(),
    }
    return HttpResponse(json.dumps(ret))


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
