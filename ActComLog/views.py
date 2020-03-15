from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from .models import ACL

def index(request):
    all_acl = ACL.objects.all()
    return render(request, 'ActComLog/index.html', {'all_acl':all_acl})

def submit_data(request):
    if request.method=="POST":
        day_to_day_message = request.POST['day_message']
        long_message = request.POST['long_message']
        dates_to_remember = request.POST['dates_to_remember']
        print(dates_to_remember)
        print(long_message)
        print(day_to_day_message)
        acl = ACL(day_to_day_message=day_to_day_message, long_term_message=long_message, dates_to_remember=dates_to_remember)
        acl.save()        
    return redirect(reverse('ActComLog:index'))