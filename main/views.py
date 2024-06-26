import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from .forms import TodoItemForm
from .models import ToDoNote


def index(request):

    form = TodoItemForm()

    if request.user.is_authenticated:
        items = ToDoNote.objects.filter(user=request.user)

    elif request.session.session_key:
        items = ToDoNote.objects.filter(session_key=request.session.session_key)

    else:
        items = None

    context = {
        'title': 'Главная страница',
        'items': items,
        'form': form
    }
    return render(request=request, template_name='main/index.html', context=context)


@require_POST
def note_add(request):
    form = TodoItemForm(data=request.POST)
    if form.is_valid():
        if request.user.is_authenticated:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        else:
            if not request.session.session_key:
                request.session.create()
            instance = form.save(commit=False)
            instance.session_key = request.session.session_key
            instance.save()
    return redirect('main:index')


def note_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        try:
            item = ToDoNote.objects.get(pk=item_id)
            item.delete()
            return JsonResponse({'success': True})
        except ToDoNote.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Объект не найден'}, status=404)

    return JsonResponse({'success': False, 'error': 'Некорректный запрос'}, status=400)


def note_check(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        try:
            note = ToDoNote.objects.get(pk=item_id)
            if note.is_completed:
                note.is_completed = False
            else:
                note.is_completed = True
            note.save()
            return JsonResponse({'success': True})
        except ToDoNote.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Объект не найден'}, status=404)
    return JsonResponse({'success': False, 'error': 'Некорректный запрос'}, status=400)