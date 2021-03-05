from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

GENRE_TYPE = (
    ('Soulful house', 'Soulful House'),
    ('Dub', 'Dub'),
    ('Deep House', 'Deep House'),
    ('Afro', 'Afro'),
)

class Track(models.Model):
    song = models.FileField(upload_to='music/')
    artwork = models.ImageField(
        upload_to='artwork/', default=None, blank=True, null=True)
    name = models.CharField(max_length=100, null=True, unique=True)
    artist = models.CharField(max_length=100, default=None, unique=True)
    genre = models.CharField(max_length=100, default="house", choices=GENRE_TYPE)
    date = models.DateField(auto_now_add=True)
    playlist = models.ManyToManyField('Playlist', related_name="tracks")
    

    def __str__(self):
        return str(self.artist) + " <---> " + str(self.name)

    def get_absolute_url(self):
        return reverse("app:track_detail", kwargs={"pk": self.pk})

    @property
    def songURL(self):
        try:
            url = self.song.url
        except:
            url = ''
        return url

    @property
    def artworkURL(self):
        try:
            url = self.artwork.url
        except:
            url = ''
        return url


class Playlist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, default=None, max_length=100)
    artwork = models.ImageField(
        upload_to='playlist/', default=None, blank=True, null=True)
    featured = models.BooleanField(default=False, null=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse("app:playlist", kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    
    @property
    def playlistartwork(self):
        try:
            url = self.artwork.url
        except:
            url = ''
        return url


