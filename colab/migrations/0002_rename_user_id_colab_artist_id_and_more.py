# Generated by Django 5.0.2 on 2024-03-04 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colab', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colab',
            old_name='user_id',
            new_name='artist_id',
        ),
        migrations.RenameField(
            model_name='colab',
            old_name='colab_audio',
            new_name='audio',
        ),
        migrations.RenameField(
            model_name='colab',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='colab',
            old_name='colab_picture',
            new_name='song_picture',
        ),
        migrations.RenameField(
            model_name='colab',
            old_name='colab_video',
            new_name='video',
        ),
    ]
