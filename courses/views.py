from itertools import chain

from django.shortcuts import render, get_object_or_404

from . import models


def course_list(request):
    courses = models.Course.objects.all()
    email = 'urosh43@gmail.com'
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})


def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(course.video_set.all(), key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {'course': course, 'steps': steps})


def video_detail(request, course_pk, step_pk):
    video = get_object_or_404(models.Video, course_id=course_pk, pk=step_pk)
    quiz = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/video_detail.html', {'video':video, 'quiz':quiz})


def quiz_detail(request, course_pk, step_pk):
    quiz = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/quiz_detail.html', {'quiz':quiz})