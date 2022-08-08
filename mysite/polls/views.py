from multiprocessing import context
from re import template
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question, Choice
from django.template import loader
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name: str = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pubDate')[:5]
    
    
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.Choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))