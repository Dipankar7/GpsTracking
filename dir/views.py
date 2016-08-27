from django.shortcuts import render,redirect,render_to_response
from .forms import detailsForm
from django.db import connection
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'example.html',{})

# def getDetails(request):
#     if request.method=="POST":
#         #form=detailsForm(request.POST)
#         print request.POST
#         return render(request,'test1.html',{})
#
#     return render(request,'formDetail.html',{})
#
# def getDetails(request):
#     context={}
#     if request.method=="POST":
#         form=detailsForm(request.POST)
#         if form.is_valid():
#             print "form is valid"
#             data=form.cleaned_data
#             startTime=data['start_time']
#             endTime=data['end_time']
#             print startTime,endTime
#             cursor = connection.cursor()
#             if cursor.execute("select longitude/10000000000,latitude/10000000000,UNIX_TIMESTAMP(position_datetime),speed from  tracklog_795_3577_history where now > %s and now < %s order by now;",[startTime,endTime]):
#                 geoDataTemp=cursor.fetchall()
#                 geoData=[]
#                 timeData=[]
#                 for i in geoDataTemp:
#                     temp=[]
#                     temp.append(float(i[1]))
#                     temp.append(float(i[0]))
#                     geoData.append(temp)
#                     tempTime=[]
#                     tempTime.append(float(i[2]))
#                     tempTime.append(int(i[3]))
#                     timeData.append(tempTime)
#                 print geoData[0]
#                 sumSec=0
#                 initialTime=timeData[0][0]
#                 currentTime=initialTime
#                 for j in range(len(timeData)):
#                     if timeData[j][1]!=0:
#                         sumSec=sumSec+(timeData[j][0]-currentTime)
#                         currentTime=timeData[j][0]
#                     else:
#                         currentTime=timeData[j][0]
#
#
#
#                 m, s = divmod(sumSec, 60)
#                 h, m = divmod(m, 60)
#                 timeReq="%d:%02d:%02d" % (h, m, s)
#                 print timeReq
#
#                 print sumSec/3600
#
#
#                 context["geoData"]=geoData
#                 context["TimeReq"]=timeReq
#                 context["HrTime"]=sumSec/3600
#
#             return render(request,'demo.html',context)
#     else:
#         form=detailsForm()
#
#     return render(request,'formDetail.html',{'form':form})

def checkSnake(request):
    context={}
    cursor = connection.cursor()
    startTime='2016-08-24 15:22:36'
    endTime='2016-08-24 21:27:43'
    if cursor.execute("select longitude/10000000000,latitude/10000000000 from  tracklog_795_3577_history where now > %s and now < %s order by now;",[startTime,endTime]):
        geoDataTemp=cursor.fetchall()
        geoData=[]
        for i in geoDataTemp:
            temp=[]
            temp.append(float(i[1]))
            temp.append(float(i[0]))
            geoData.append(temp)
        context["geoData"]=geoData
    return render(request,'demo.html',context)

def getDetails(request):
    print request.method
    context={}
    print "form is valid"
    print request.POST
    startTime=request.POST.get('startDate')
    endTime=request.POST.get('endtDate')
    print startTime,endTime
    cursor = connection.cursor()
    if cursor.execute("select longitude/10000000000,latitude/10000000000,UNIX_TIMESTAMP(position_datetime),speed from  tracklog_795_3577_history where now > %s and now < %s order by now;",[startTime,endTime]):
        geoDataTemp=cursor.fetchall()
        print geoDataTemp
        geoData=[]
        timeData=[]
        for i in geoDataTemp:
            temp=[]
            temp.append(float(i[1]))
            temp.append(float(i[0]))
            geoData.append(temp)
            tempTime=[]
            tempTime.append(float(i[2]))
            tempTime.append(int(i[3]))
            timeData.append(tempTime)
        print geoData[0]
        sumSec=0
        initialTime=timeData[0][0]
        currentTime=initialTime
        for j in range(len(timeData)):
            if timeData[j][1]!=0:
                sumSec=sumSec+(timeData[j][0]-currentTime)
                currentTime=timeData[j][0]

            else:
                currentTime=timeData[j][0]



        m, s = divmod(sumSec, 60)
        h, m = divmod(m, 60)
        timeReq="%d:%02d:%02d" % (h, m, s)
        print timeReq
        print sumSec/3600


        context["geoData"]=geoData
        context["TimeReq"]=timeReq
        context["HrTime"]=sumSec/3600

    return render(request,'demo.html',context)


def new1(request):
    return render(request,"new.html",{})


