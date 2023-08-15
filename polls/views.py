from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Choice, Question
from .forms import CreatePollForm

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Question.DoesNotExisty):
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))

def create_poll(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question']
            choices_text = form.cleaned_data['choices']
            choices = [choice.strip() for choice in choices_text.split(',')]
            pub_date = form.cleaned_data['pub_date']
            
            question = Question.objects.create(question_text=question_text, pub_date=pub_date)
            for choice in choices:
                Choice.objects.create(question=question, choice_text=choice)
            
            return redirect('polls:index')
    else:
        form = CreatePollForm()
    
    return render(request, 'polls/create_poll.html', {'form': form})