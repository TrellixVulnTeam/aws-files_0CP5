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
    
    #print(request.POST)
    if request.method == 'POST':  
        questions=request.POST.get('question')
        answers=request.POST.get('answer')
        q=Question(text=questions,answer=answers)
        if questions=='' or answers=='':
            return render(request,'create_question_failure.html')
        else:
            q.save()
            return render(request,'create_question_success.html')
    elif request.method == 'GET':
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
    q = Question.objects.get(pk=question_id)
    questions=request.POST.get('question')
    answers=request.POST.get('answer')
    if questions=='' or answers=='':
        return render(request,'update_question_failure.html')
    else:
        q.text=questions
        q.answer=answers
        q.save()
        return render(request,'update_question_success.html')

def delete_question(request, question_id):
    #delete_question_success.html
    #return HttpResponse('')
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return render(request,'delete_question_failure.html')
    q.delete()
    return render(request,'delete_question_success.html')
    #q.delete()
    
    ''' list1=[]
    q2=Question.objects.all()
    for i in q2:
        list1.append(i.id)
        
    if question_id in list1:
        q = Question.objects.get(pk=question_id)
        q.delete()
        return render(request,'delete_question_success.html')
    else:
        return render(request,'delete_question_failure.html')'''
