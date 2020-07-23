# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

def get_list_of_questions(request):
    #return render(request,'get_list_of_questions.html')
    
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'get_list_of_questions.html', context)

def create_question(request):
    
    print(request.POST)
    
    if request.method == 'POST':
        questions=request.POST.get('question')
        answers=request.POST.get('answer')
        q=Question(text=questions,answer=answers)
        
        if questions=='' or answers=='':
            return render(request,'create_question_failure.html')
        else:
            q.save()
            return render(request,'create_question_success.html')
    return render(request,'create_question_form.html')

def get_question(request, question_id):
    #each_question_form.html
    
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'each_question_form.html', {'question': question})
    #return (request,'each_question_form.html')

def update_question(request, question_id):
    #update_question_success.html
    #return HttpResponse('')
    ids = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        questions=request.POST.get('question')
        answers=request.POST.get('answer')

def delete_question(request, question_id):
    #delete_question_success.html
    return HttpResponse('')

