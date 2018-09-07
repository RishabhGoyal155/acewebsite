# Generated by Django 2.1.1 on 2018-09-07 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0005_auto_20180907_0921'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='poc',
        ),
        migrations.AddField(
            model_name='event',
            name='pictures',
            field=models.ManyToManyField(blank=True, null=True, to='portalapp.ACEUserProfile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photos',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='events_pictures', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_pictures', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ManyToManyField(blank=True, null=True, to='portalapp.ACEUserProfile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_screenshot', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]