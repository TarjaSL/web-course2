from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')
	
def new_quest(request):
    questions = Question.objects.order_by('-id')
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/question/all_posts/?page='
    page = paginator.page(page) # Page
    return render(request, 'ask/quest_list.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def popular_quest(request):
    questions = Question.objects.order_by('-rating')
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/question/all_posts/?page='
    page = paginator.page(page) # Page
    return render(request, 'ask/popular_list.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })
	
def quest_details(request, pk):
	try:
		question = Question.objects.get(id=pk)
	except question.DoesNotExist:
		raise Http404
	answers = question.answer_set.all()
	return render(request, 'ask/quest_details.html', {'question': question,
	'answers': answers,
	})

	
