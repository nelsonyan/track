

from django.shortcuts import render
from .forms import IssueInput
from django import forms
from .models import TrackHeader
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import UpdateView, DeleteView, ListView
from django.urls import reverse_lazy, reverse


def TrackReport(request):
    report_output = TrackHeader.objects.order_by('-report_key')
    return render(request, 'report.html', {'report_output': report_output})


def TrackInput(request):
    report_input = IssueInput()
    if request.method =='POST':
        report_input = IssueInput(request.POST)
        if report_input.is_valid():
            report_input.save(commit = True)
            return HttpResponseRedirect(reverse('report:track_report'))
        else:
            print('Error in input')
    return render(request, 'report_input.html', {'report_input': report_input})


class TrackUpdate(UpdateView):

    model = TrackHeader
    template_name = 'report_detail.html'
    context_object_name = 'form_delete'
            #re-create input form
            #tag is still 'form' by default cannot change, it is teid to <form> input?
            #'form_delete' is used to pass PK into delete function
    form_class = IssueInput
        # fields = '__all__'
            #don;t use this if maunal form class is passed in
        #this is how form widgets can be passed into classbase view
        #holy fuck did I just do it 9/7/2018 is the best day of 2018
    # widgets = {
        # 'comments': forms.Textarea(attrs={'rows':15, 'cols':90}),
            #this changes the size of text area
    # }
        # no need to do it here again, IssueInput already has widgets defined, but this is another place to do widget

class TrackDelete(DeleteView):
    model = TrackHeader
    success_url = reverse_lazy('report:track_report')
        #only run this when the submit is pressed in 'trackheader_confirm_delete'
    context_object_name = 'report_delete'


import csv
def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datas.csv"'

    writer = csv.writer(response)
    writer.writerow(['report_key', 'category', 'task_name', 'dead_line', 'requested_by', 'date_requested',
        'assigned_to', 'status', 'sku_count', 'sell_sheet', 'pog_render', 'artwork_design', 'mockup', 'comments',])

    export_tracks = TrackHeader.objects.all().values_list('report_key', 'category', 'task_name', 'dead_line', 'requested_by', 'date_requested',
        'assigned_to', 'status', 'sku_count', 'sell_sheet', 'pog_render', 'artwork_design', 'mockup', 'comments',)
    for export_track in export_tracks:
        writer.writerow(export_track)

    return response
