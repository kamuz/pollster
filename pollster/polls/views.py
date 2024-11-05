from django.shortcuts import render
from .models import Question, Choice

# Get and display questions
def index(request):
	return render(request, 'polls/index.html')
