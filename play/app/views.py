from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import View, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import ArtistForm, TrackForm
from .models import Track, Playlist


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        playlists = Playlist.objects.all()
        featured_playlist = playlists.filter(featured='True')
        print(featured_playlist)
        context = {'featured_playlist': featured_playlist}
        return render(request, self.template_name, context)


# class ProfileView(LoginRequiredMixin, View):
#     template_name = 'core/profile.html'
#     context_object_name = 'user'
#     model = User
#     queryset = User.objects.all()

#     def get(self, request):
#         user = request.user
#         Artist.objects.get_or_create(user=user)
#         artist = request.user.artist

#         context = {
#             'artist': artist
#         }
#         return render(request, self.template_name, context)


# @login_required(login_url='account_login')
# def artistFormView(request):
#     artist = request.user.artist
#     form = ArtistForm(instance=artist)
#     if request.method == "POST":
#         form = ArtistForm(request.POST, request.FILES, instance=artist)
#         if form.is_valid():
#             form.save()
#             return redirect('core:profile')

#     context = {'form': form}
#     return render(request, 'core/forms/artist_form.html', context)


# @login_required(login_url='account_login')
# def uploadTrackFormView(request):
#     artist = request.user.artist
#     print(artist)
#     form = TrackForm(initial={'artist': artist})
#     if request.method == "POST":
#         form = TrackForm(request.POST, request.FILES,
#                          initial={'artist': artist})
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('core:track_detail', kwargs={'pk': form.instance.pk}))

#     context = {'form': form}
#     return render(request, 'core/forms/track_form.html', context)


class PlaylistsView(LoginRequiredMixin, View):
    template_name = 'core/tracks.html'
    queryset = Playlist.objects.all()
    model = Playlist

    def get(self, request):
        playlists = self.queryset
        search_str = request.GET.get('search_input')
        if search_str != '' and search_str is not None:
            playlists = playlists.filter(name__icontains=search_str)

        context = {
            'playlists': playlists,
        }
        return render(request, self.template_name, context)


class PlaylistView(LoginRequiredMixin, DetailView):
    context_object_name = 'playlist'
    model = Playlist
    queryset = Playlist.objects.all()
    template_name = 'core/track_detail.html'
    pk_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.pk_url_kwarg)
        if slug is not None:
            queryset = queryset.filter(slug=slug)

        return get_object_or_404(self.model, slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tracks"] = self.object.tracks.order_by("?") # order_by causes shuffle behaviour
        return context


# class ArtistView(LoginRequiredMixin, DetailView):
#     context_object_name = 'artist'
#     model = Artist
#     queryset = Artist.objects.all()
#     template_name = 'core/artist.html'
#     pk_url_kwarg = 'pk_test'

#     def get_object(self, queryset=None):
#         if queryset is None:
#             queryset = self.get_queryset()

#         pk_test = self.kwargs.get(self.pk_url_kwarg)
#         if pk_test is not None:
#             queryset = queryset.filter(pk=pk_test)

#         return get_object_or_404(self.model, pk=pk_test)
