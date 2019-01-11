from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Albums
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Albums.objects.all()


class DetailView(generic.DetailView):
    model = Albums
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Albums
    fields = ['artist', 'genre', 'album_title', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Albums
    fields = ['artist', 'genre', 'album_title', 'album_logo']


class AlbumDelete(DeleteView):
    model = Albums
    success_url = reverse_lazy('Music:index')
    fields = ['artist', 'genre', 'album_title', 'album_logo']


class UserFormView(View):
    form_class = UserForm
    template_name = 'Music/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns Usr Objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return  redirect('Music:index')

        return render(request, self.template_name, {'form': form})
