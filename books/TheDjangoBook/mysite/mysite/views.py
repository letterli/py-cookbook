from django.http import HttpResponse
from django.shortcuts import render_to_response

from datetime import datetime, timedelta


def hello(request):
    return HttpResponse("Hello World.")


def currentTime(request):
    now = datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)


def plusTime(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    plusTime = datetime.now() + timedelta(hours=offset)
    html = '<html><body>In %s hours, it will be %s.</body></html>' % (offset, plusTime)
    return HttpResponse(html)


def renderTemplate(request):
    now = datetime.now()
    return render_to_response('render_template.html', {'currentTime' : now})


def UADisplay(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Your browser is %s." % ua)


def requestInfo(request):
    info = request.META.iteritems()
    return render_to_response('request_info.html', locals())


def yearArchive(request, year):
    return HttpResponse("Year: %s" % year)


def monthArchive(request, year, month):
    return HttpResponse("Year: %s, Month: %s" % (year, month))


def userInfo(request, userId):
    return HttpResponse('User %s is login!' % userId)

def login(request):
    return HttpResponse('Need login!')
