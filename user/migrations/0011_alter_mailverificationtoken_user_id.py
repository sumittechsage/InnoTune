# Generated by Django 5.0.2 on 2024-06-01 08:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_mailverificationtoken_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailverificationtoken',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verification_token', to=settings.AUTH_USER_MODEL),
        ),
    ]
