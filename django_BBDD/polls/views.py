from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def roomId(request, question_id):
    response = "You're looking at the results of id %s."
    return HttpResponse(response % question_id)