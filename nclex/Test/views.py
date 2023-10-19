from django.shortcuts import render
from .models import Question
from django import forms

class MCQForm(forms.Form):
    choice = forms.ChoiceField(widget=forms.RadioSelect)

def test(request):
    questions = Question.objects.all()
    form = MCQForm()
    if request.method == 'POST':
        form = MCQForm(request.POST)
        if form.is_valid():
            print("posted done")
            selected_choice = form.cleaned_data['choice']
            ans = Question.objects.get(ques=selected_choice).ans

            # Check if the selected choice matches the correct answer
            if selected_choice == ans:
                print("correct")
            else:
                print("wrong")

    return render(request, 'test/home.html', {'form': form, 'questions': questions})
