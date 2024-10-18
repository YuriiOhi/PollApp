# Importing necessary modules and functions
from django.db.models import F
from django.http import Http404
from .models import Choice, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader   # For loading templates (not used in this code)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
    
    
# The vote view: Handles voting on a specific question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


