# Generated by Django 2.1 on 2019-08-27 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190827_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue_performer', to=settings.AUTH_USER_MODEL),
        ),
    ]