# Generated by Django 2.2.6 on 2019-11-11 10:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0003_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='exact_location',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notice',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.Profile'),
        ),
    ]
