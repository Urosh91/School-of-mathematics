from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from courses import models
from . import forms


def welcome(request):
    courses = models.Course.objects.all()
    return render(request, 'home.html', {'courses': courses})


@login_required#(login_url='/login/')
def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
        if form.is_valid():
            send_mail(
                f'Suggestion from {form.cleaned_data["name"]}',
                form.cleaned_data['suggestion'],
                f'{form.cleaned_data["name"]} <{form.cleaned_data["email"]}>',
                ['urosh43@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS, 'Thank you for your suggestion')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})
