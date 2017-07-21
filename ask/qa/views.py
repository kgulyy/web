from django.http import HttpResponse


def test(request, question_id):
    return HttpResponse('OK')
