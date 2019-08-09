from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

from django.template import loader


def home(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "body/home.html", data)


def main_page(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    data = {"header": "Last questions", "message": output}
    print(output)

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('body/main_page.html')
    context = {
        'latest_question_list': latest_question_list,
        'header': 'Last questions',
        'message': output,
    }
    print(latest_question_list)
    # return render(request, "body/main_page.html", data)
    return HttpResponse(template.render(context, request))


def sing_in(request):
    if request.method == "GET":
        return render(request, "body/sing_in.html")
    elif request.method == "POST":
        print(request.POST)
        return render(request, "body/sing_in.html")


def sing_up(request):
    return render(request, "body/sing_up.html")


def tasks(request):
    return render(request, "body/tasks.html")


def settings(request):
    return render(request, "body/settings.html")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


