# Generated by Django 3.2.9 on 2021-11-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=3),
        ),
    ]
