from django.shortcuts import render
from . import forms
from django.shortcuts import render,redirect
from . models import Questionnaire
from django.contrib.auth.decorators import login_required

# Create your views here.
def set_questions(request):
    return render(request,'questionnaire/set_questions.html')
@login_required(login_url="/accounts/login/")
def question_create(request):
    if request.method=='POST':
        form=forms.CreateQuestions(request.POST,request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form=forms.CreateQuestions()
    return render(request, 'qusetionnaire/question_create.html',{'form':form})