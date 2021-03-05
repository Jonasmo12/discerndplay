# Generated by Django 3.1.7 on 2021-03-05 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(default=None, max_length=100, unique=True)),
                ('artwork', models.ImageField(blank=True, default=None, null=True, upload_to='playlist/')),
                ('featured', models.BooleanField(default=False, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(upload_to='music/')),
                ('artwork', models.ImageField(blank=True, default=None, null=True, upload_to='artwork/')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('artist', models.CharField(default=None, max_length=100, unique=True)),
                ('genre', models.CharField(choices=[('Soulful house', 'Soulful House'), ('Dub', 'Dub'), ('Deep House', 'Deep House'), ('Afro', 'Afro')], default='house', max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('playlist', models.ManyToManyField(related_name='tracks', to='app.Playlist')),
            ],
        ),
    ]