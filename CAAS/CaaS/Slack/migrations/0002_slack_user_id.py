# Generated by Django 2.2 on 2020-01-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slack',
            name='user_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
