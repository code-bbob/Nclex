from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random
from django.contrib import messages

# Create your views here.

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    selected_categories = request.GET.get('scategory')
    if selected_categories:
        return redirect(f'/quiz/quiz/?category={selected_categories}')

    return render(request,'quiz/home.html', context)


def get_quiz(request):
    question_objs= list(Question.objects.all())
    
    if request.GET.get('category'):
        question_objs= Question.objects.filter(category__category_name__icontains=request.GET.get('category')) #esma xai request.GET.get le category=coding lekhya thyo vane tyo category vanya ho so it could have been bibhab= coding and i cld write request.GET.get('bibhab') ani tala category__category_name ma xai class ko data members haru lekhya ho and end ma i contains = paxi xai bibhab lekhda hunthyo

    question_objs = list(question_objs)
    data = []
    random.shuffle(question_objs)   
    for question_obj in question_objs:
        data.append({
            "category": question_obj.category.category_name,
            "question": question_obj.question,
            "marks": question_obj.marks,
            "answer":question_obj.get_answer(),

        })



    payload= {'status': True,
              'data': data}
    return JsonResponse(payload)

import ast
import json
def quiz(request):

    selected_category = request.GET.get('category')
    if request.method == 'POST':
        selected_category = request.POST.get('selected_category')
        current_question_id = request.POST.get('current_question')
        selected_answer_id = request.POST.get('answer')
        solved_questions = ast.literal_eval(request.POST.get('solved_questions'))   
        current_question = Question.objects.get(pk=current_question_id)
        correct_answer = Answer.objects.filter(question=current_question, is_correct=True).first()
        correct_answer_id = correct_answer.id

        next_question = []
        solved_questions.add(current_question_id)
        # solved_questions = [ int(q) for q in solved_questions]
        print("solved_questions",solved_questions)
        print("selected_category",selected_category)
        if selected_answer_id == str(correct_answer_id):
            print(Question.objects.filter(category__category_name=selected_category))
            if solved_questions:
                next_question = Question.objects.filter(category__category_name=selected_category).exclude(id__in=solved_questions)
                next_question = list(next_question)
                random.shuffle(next_question)
               
            if next_question:
                next_question = next_question[0]
                next_question_answers = list(next_question.question_answer.all())
                random.shuffle(next_question_answers)
                return render(request, 'quiz/quiz.html', {'selected_category': selected_category, 'question': next_question, 'solved_questions': solved_questions, 'shuffled_answers': next_question_answers})
            # next_question = Question.objects.filter(category__category_name=selected_category, pk__gt=current_question_id).first()
                
            else:
                # User has completed all questions
                return HttpResponse("Congratulations! You have completed the quiz.")
        else:
            messages.error(request,"Please Select Correct Answer")
            return render(request, 'quiz/quiz.html', {'selected_category': selected_category,'question': current_question,'solved_questions':solved_questions})


    question = Question.objects.filter(category__category_name=selected_category).first()
    print (question)
    context = {
        'selected_category': selected_category,
        'question': question,
        "solved_questions":set()
    }
    return render(request,'quiz/quiz.html', context)
