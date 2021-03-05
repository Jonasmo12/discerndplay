from django.contrib import admin
from .models import Track, Playlist
# Register your models here.

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Track)