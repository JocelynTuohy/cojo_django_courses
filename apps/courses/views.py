# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    print 'Baddabing Baddaboom by Earl'
    return render(request, 'courses/index.html')
