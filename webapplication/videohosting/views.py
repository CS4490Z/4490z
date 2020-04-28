from datetime import timezone
from django.shortcuts import render, render_to_response
from django.views import View
from .models import RecordingSet
from .models import WorkingSet
from datetime import date



class CreatePost(View):
    def post(self, request):
        postlist = request.POST.getlist('n')
        length = len(postlist)
        i = 0
        obj = WorkingSet.objects.all()
        todaysDate=date.today();
        while i < length:
            newlist = postlist[i].split('divider')
            if newlist[17] == 'saveRecordingSet':
                print("newlist",newlist)
                record = RecordingSet(identifier=newlist[18], category=newlist[0], tag=newlist[1],
                                      url=newlist[2], abort=newlist[6], ended=newlist[7],
                                      error=newlist[8], pause=newlist[16], play=newlist[9],
                                      playing=newlist[10], seeked=newlist[11], seeking=newlist[12],
                                      timeupdate=newlist[13], volumechange=newlist[14], waiting=newlist[15],
                                      rating=newlist[3], timestopped=newlist[5], comment=newlist[4],
                                      date=todaysDate)
                record.save()
            if newlist[17] == 'saveWorkingSet':
                if (i==0):
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
