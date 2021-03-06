# Generated by Django 3.1.1 on 2020-09-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
