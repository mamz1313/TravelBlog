# Generated by Django 4.1.3 on 2022-11-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0008_alter_post_options_alter_tags_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='id_post',
        ),
        migrations.AddField(
            model_name='tags',
            name='id_post',
            field=models.ManyToManyField(default=1, to='AppBlog.post'),
        ),
    ]