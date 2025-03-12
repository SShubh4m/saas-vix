from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit
this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "My Page!"
    html_template = "home.html"
    my_context = {
        "page_title" : my_title,
        "page_visit_count" : page_qs.count(),
        "total_visit_count" : qs.count(),
        "percent" : (page_qs.count() * 100 / qs.count())
    }
    path = request.path
    print("path", path)
    print(this_dir)
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)
