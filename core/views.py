from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, '01_base/base.html', locals())


def chapeudepalha_html(request):
    context = {}

    load_template = request.path
    template = loader.get_template('00_materialDesign/' + load_template)
    return HttpResponse(template.render(context, request))