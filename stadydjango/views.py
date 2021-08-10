from django.http import HttpResponse


def hello_views(request):
    html = "<h1>欢迎来到得来联盟</h1>"
    return HttpResponse(html)


def page_2003_views(request):
    html = "<h1>2003年</h1>"
    return HttpResponse(html)


def page_num_views(request, year, msg, pa, slug):
    html = f"<h1>{year}年, {msg}, {pa}, {slug}</h1>"
    return HttpResponse(html)
