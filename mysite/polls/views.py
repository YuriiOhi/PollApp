# Importing necessary modules and functions
from django.http import Http404
from .models import Question
from django.http import HttpResponse  # For returning HTTP responses
from django.template import loader   # For loading templates (not used in this code)
from django.shortcuts import render  # For rendering templates with context data

# Importing the Question model from the current app's models.py
from .models import Question

# The index view: Displays the latest 5 questions
def index(request):
    # Query the database to get the latest 5 questions ordered by publication date
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # Create a context dictionary to pass to the template
    context = {"latest_question_list": latest_question_list}
    # Render the "polls/index.html" template with the context data
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


# The detail view: Displays a specific question based on its ID
def detail(request, question_id):
    # Returns a simple text response with the question ID
    return HttpResponse("You're looking at question %s." % question_id)

# The results view: Displays the results of a specific question
def results(request, question_id):
    # Create a response string that includes the question ID
    response = "You're looking at the results of question %s."
    # Returns the response as an HTTP response
    return HttpResponse(response % question_id)

# The vote view: Handles voting on a specific question
def vote(request, question_id):
    # Returns a simple text response acknowledging the vote for a question
    return HttpResponse("You're voting on question %s." % question_id)
