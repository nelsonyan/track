

from django.shortcuts import render
from django.views.generic import View
from report.forms import PublicCommentForm
from report.models import PublicComment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# Create your views here.

# class HomePage(View):
    # def get(self, request):
        # return render(request, 'home.html')
            #once the app is included in the install app on setting.py, templates folder becomes default location

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
        #-id can be used even as default value
        #if missing order_by, errror is manager object is not iterable
    comment = {
        'comment_output': comment_output,
        'comment_input': comment_input
    }
    return render(request, 'home.html', comment)
        #one url one view one page but two template tags
