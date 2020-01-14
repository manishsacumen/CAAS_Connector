# Generated by Django 2.2 on 2020-01-09 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jira', '0007_remove_jira_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jira',
            name='user_id',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
