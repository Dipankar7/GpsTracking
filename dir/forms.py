from django import forms
import datetime
#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

from django.contrib.admin.widgets import AdminDateWidget

#import re


class detailsForm(forms.Form):
    name=forms.CharField(max_length=100)
    # startDateTime=forms.DateTimeField(widget=SelectDateTimeWidget)
    # endDateTime=forms.DateTimeField(widget=SelectDateTimeWidget)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()


    # def clean(self):
    #     data=self.cleaned_data['phoneNumber']
    #     data_arr=data.split(",")
    #     print "came in validation"
    #     for i in data_arr:
    #         if(re.match(r'^\+91[0-9]+$',i)):
    #             if(len(i)!=13):
    #                 errorText=i+" this number entered is less than 10 digits"
    #                 raise forms.ValidationError(errorText)
    #         else:
    #             x=re.match(r'^[0-9]+$',i)
    #             if not x:
    #                 errorText=i+" this number entered is not in proper format"
    #                 raise forms.ValidationError(errorText)
    #             elif len(i)!=10:
    #                 errorText=i+" this number entered is less than 10 digits"
    #                 raise forms.ValidationError(errorText)
    #
    #     return data
