from django.shortcuts import render, get_object_or_404
from .models import Albums



def index(request):
    all_albums = Albums.objects.all()
    return render(request, 'Music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    albums = get_object_or_404(Albums,pk=album_id)
    return render(request, 'Music/detail.html', {'albums': albums})

def favorite(request, album_id):
    albums = get_object_or_404(Albums, pk=album_id)
    try:
        selected_song = albums.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'Music/detail.html',
                      {'albums': albums,
                       'error_message': "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'Music/detail.html', {'albums': albums})