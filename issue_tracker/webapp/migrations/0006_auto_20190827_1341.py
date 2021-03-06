# Generated by Django 2.1 on 2019-08-27 13:41

from django.db import migrations

def update_authors(apps, shema_editor):
    User = apps.get_model('auth', 'User')
    Issue = apps.get_model('webapp', 'Issue')
    admin = User.objects.first()
    Issue.objects.all().update(author=admin)


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190827_1337'),
    ]

    operations = [
        migrations.RunPython(update_authors),
    ]
