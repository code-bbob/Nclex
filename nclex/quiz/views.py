from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random

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


def quiz(request):
    selected_category = request.GET.get('category')

    questions = Question.objects.filter(category__category_name=selected_category)
    context = {
        'selected_category': selected_category,
        'questions': questions,
    }
    return render(request,'quiz/quiz.html', context)