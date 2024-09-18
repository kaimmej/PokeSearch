from django.db.models import F

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse("Hello, world. You're at the polls index.")


    context = {
        "latest_question_list": latest_question_list,
    }
    # /polls/index.html template is pulled in through the render function
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))


    # RENDER( ... ) It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provides a shortcut.
    return render(request, "polls/index.html", context)

def detail(request, question_id):

    """
        LONG WAY
            This try-catch checks whether the object with that PK exists. And if it doesn't, it raises a 404 error.
            But the django.API provides a shortcut. You can use the get_object_or_404() function.
    """
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question does not exist")
    


    # SHORTCUT 
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})







    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice.set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "you didn't select a choice",
            },
        )
    else:

        # WHAT THE HECK IS "F"??
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))




    return HttpResponse("You are voting on question %s." % question_id)