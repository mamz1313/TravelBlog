# Generated by Django 4.1.3 on 2022-11-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0010_alter_post_options_alter_tags_id_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='id_post',
            field=models.ManyToManyField(default=1, to='AppBlog.post'),
        ),
    ]