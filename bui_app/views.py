# encoding:utf-8

import json
import logging
import time

from django.shortcuts import render

# Create your views here.

log_info1 = logging.getLogger("bui_log1")


def index(request):
    print("request index ..")
    return render(request, "index.html", locals())


def index_layout(request):
    return render(request, "index_layout.html", locals())


def index_tree(request):
    return render(request, "index_tree.html", locals())
