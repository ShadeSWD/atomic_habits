# Generated by Django 4.2.7 on 2023-11-24 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='action',
            field=models.CharField(default=1, max_length=50, verbose_name='action'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habit',
            name='award',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='award'),
        ),
        migrations.AddField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=1, verbose_name='is public'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habit',
            name='period',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=1, verbose_name='periodicity'),
        ),
        migrations.AddField(
            model_name='habit',
            name='time_for_action',
            field=models.DurationField(verbose_name='time for action'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='habit',
            name='connected_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='habit.habit', verbose_name='connected pleasant habit'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
            preserve_default=False,
        ),
    ]
