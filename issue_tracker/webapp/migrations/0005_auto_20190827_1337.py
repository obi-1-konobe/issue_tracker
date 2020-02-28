# Generated by Django 2.1 on 2019-08-27 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190725_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issues', to=settings.AUTH_USER_MODEL),
        ),
    ]