from datetime import timezone
from django.http import JsonResponse

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import RecordingSet
from .models import WorkingSet
from .models import DistractionSet
from datetime import date


class CreatePost(View):
    def post(self, request):
        postlist = request.POST.getlist('n')
        distractionList = request.POST.getlist('sendDistractionTag')
        clearDistractionList = request.POST.getlist('clearDistractionTag')

        if (clearDistractionList[0]!='false'):
            DistractionSet.objects.all().delete()

        if (distractionList[0]!='false'):
            splittedList= distractionList[0].split('divider')
            distractModel=DistractionSet(vidCategory = splittedList[0],
                                        vidTag = splittedList[1],
                                        vidURL = splittedList[2])
            distractModel.save()
        length = len(postlist)
        i = 0
        obj = WorkingSet.objects.all()
        todaysDate = date.today();
        while i < length:
            newlist = postlist[i].split('divider')
            if newlist[17] == 'saveRecordingSet':
                record = RecordingSet(identifier=newlist[18], category=newlist[0], tag=newlist[1],
                                      url=newlist[2], abort=newlist[6], ended=newlist[7],
                                      error=newlist[8], pause=newlist[16], play=newlist[9],
                                      playing=newlist[10], seeked=newlist[11], seeking=newlist[12],
                                      timeupdate=newlist[13], volumechange=newlist[14], waiting=newlist[15],
                                      rating=newlist[3], timestopped=newlist[5], comment=newlist[4],
                                      date=todaysDate)
                record.save()
            if newlist[17] == 'saveWorkingSet':
                if (i == 0):
                    WorkingSet.objects.filter(identifier=newlist[18]).delete()
                work = WorkingSet(identifier=newlist[18], vidCategory=newlist[0], vidTag=newlist[1],
                                  vidURL=newlist[2])
                work.save()
            i = i + 1
        obj = WorkingSet.objects.all()
        return render(request, "home.html", {'obj': obj})


class LoadPost(View):
    def get(self, request):
        obj = WorkingSet.objects.all()
        return render(request, "home.html", {'obj': obj})


class ReceiveDistraction(View):
    def get(self, request):
        obj = DistractionSet.objects.all()
        return render(request, "receivedistraction.html", {'obj': obj})

class GetDistraction(View):
    def get(self,request):
        eventList = DistractionSet.objects.all()
        events = []
        # for event in eventList:
        #     events.append({"vidCategory": event.vidCategory, "vidTag": event.vidTag, "vidURL": event.vidURL})
        # return JsonResponse(events,safe=False)
        lastIndex=len(eventList)-1
        return HttpResponse(eventList[lastIndex].vidCategory+'|'+eventList[lastIndex].vidTag+'|'+eventList[lastIndex].vidURL)
        # obj = DistractionSet.objects.all()
        # lastObj= DistractionSet.objects.order_by('-id')[0]
        # lastObj
        # return HttpResponse(lastObj)
        # return render(request, 'post/index.html', { 'posts': posts })
        # return render(request, "lol.html", {'lastObj': lastObj})

