# Generated by Django 3.0.5 on 2020-05-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='message',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='lead',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
