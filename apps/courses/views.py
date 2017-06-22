# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course, Description, Comment

def index(request):
    # print 'Baddabing Baddaboom by Earl'
    context = {
        'courselist': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def addcourse(request):
    if request.method == 'POST':
        new_course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(
            description=request.POST['description'],
            course=new_course
        )
    return redirect('/')

def modifycourse(request):
    if request.method == 'POST':
        # print request.POST
        if 'removebutton' in request.POST:
            request.session['course_to_delete'] = (
                request.POST['removebutton']
            )
            return redirect('/confirmdelete')
        elif 'commentbutton' in request.POST:
            request.session['course_to_comment'] = (
                request.POST['commentbutton']
            )
            return redirect('/commentcourse')
    return redirect('/')

def confirmdelete(request):
    context = {
        'course': Course.objects.get(id=request.session['course_to_delete'])
    }
    return render(request, 'courses/confirm.html', context)

def deletecourse(request):
    if request.method == 'POST':
        # print request.POST
        if request.POST['button'] == 'delete':
            Course.objects.get(id=request.session['course_to_delete']).delete()
    return redirect('/')

def commentcourse(request):
    context = {
        'course': Course.objects.get(
            id=request.session['course_to_comment']
        ),
        'comments': Comment.objects.filter(
            course=request.session['course_to_comment']
        )
    }
    return render(request, 'courses/comments.html', context)

def addcomment(request):
    if request.method == 'POST':
        # print request.POST
        Comment.objects.create(
            content=request.POST['content'],
            course=Course.objects.get(id=request.POST['course']),
        )
    return redirect('/commentcourse')
