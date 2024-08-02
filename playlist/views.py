from django.shortcuts import render, redirect
from .models import Video

def playlist(request):
    playlist = Video.objects.all()
    return render(request, "playlist/medialist.html", {"video":playlist})

def add_video(request):
    if request.method =="POST":
        v_title = request.POST['title']
        v_embed  = request.POST['embed']
        v_decription = request.POST['description']
        Video.objects.create(
            title = v_title,
            text = v_decription,
            embed = v_embed,
        )
        return redirect('playlist')
        
        return render(request, "playlist/add_video.html")
    return render(request, "playlist/add_video.html")