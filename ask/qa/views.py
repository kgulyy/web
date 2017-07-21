from django.http import HttpResponse


def test(request):
    return HttpResponse('OK')


def question_detail(request, question_id):
    return HttpResponse('OK')
