# Generated by Django 3.0.8 on 2020-07-10 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='add',
            field=models.CharField(default='add', max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='checked',
            field=models.CharField(default='not_checked', max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='edit',
            field=models.CharField(default='edit', max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='remove',
            field=models.CharField(default='remove', max_length=20),
        ),
        migrations.AddField(
            model_name='todo',
            name='todotext',
            field=models.CharField(default='cannot_edit', max_length=20),
        ),
    ]
