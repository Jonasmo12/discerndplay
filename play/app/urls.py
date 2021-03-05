from django.urls import path
from .views import (
    HomeView,
    PlaylistsView,
    PlaylistView,
    # ArtistView,
    # ProfileView,
    # uploadTrackFormView,
    # artistFormView,
)

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('playlists/', PlaylistsView.as_view(), name='music'),
    path('playlists/<str:slug>/', PlaylistView.as_view(), name='playlist'),
    #path('music/artist/<int:pk_test>/', ArtistView.as_view(), name='artist'),
    #path('profile/', ProfileView.as_view(), name='profile'),

    #path('profile/upload/', uploadTrackFormView, name='upload_track'),
    #path('profile/artist/', artistFormView, name='artist_form'),
]
