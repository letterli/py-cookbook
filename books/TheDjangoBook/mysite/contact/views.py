# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

import logging

from forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(
            initial = {
                'subject': 'subject',
                'email': 'example@email.com',
                'message': 'your opinion'
            }
        )
    return render_to_response('contact_form.html', {'form': form})
