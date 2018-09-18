

from django.shortcuts import render
from django.views.generic import View
from report.forms import PublicCommentForm
from report.models import PublicComment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


def PublicCommentView(request):
    comment_input = PublicCommentForm()
    if request.method =='POST':
        comment_input = PublicCommentForm(request.POST)
        if comment_input.is_valid():
            comment_input.save(commit = True)
            return HttpResponseRedirect(reverse('home:home_page'))
        else:
            print('Error in input')

    comment_output = PublicComment.objects.order_by('-id')

    comment = {
        'comment_output': comment_output,
        'comment_input': comment_input
    }
    return render(request, 'home.html', comment)
    
