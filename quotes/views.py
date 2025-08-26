import random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Quote, Source
from .forms import QuoteForm
import json

def random_quote(request):
    quotes = list(Quote.objects.all())
    if not quotes:
        return render(request, 'quotes/random.html', {'quote': None})

    # Выбор с учётом веса
    weighted_quotes = []
    for quote in quotes:
        weighted_quotes.extend([quote] * quote.weight)

    chosen_quote = random.choice(weighted_quotes)
    chosen_quote.views += 1
    chosen_quote.save()

    return render(request, 'quotes/random.html', {'quote': chosen_quote})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Цитата успешно добавлена!")
            return redirect('random_quote')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add.html', {'form': form})


def top_quotes(request):
    top = Quote.objects.order_by('-likes')[:10]
    return render(request, 'quotes/top.html', {'quotes': top})


@require_POST
@csrf_exempt
def like_quote(request):
    data = json.loads(request.body)
    quote_id = data.get('id')
    quote = get_object_or_404(Quote, id=quote_id)
    quote.likes += 1
    quote.save()
    return JsonResponse({'likes': quote.likes})


@require_POST
@csrf_exempt
def dislike_quote(request):
    data = json.loads(request.body)
    quote_id = data.get('id')
    quote = get_object_or_404(Quote, id=quote_id)
    quote.dislikes += 1
    quote.save()
    return JsonResponse({'dislikes': quote.dislikes})