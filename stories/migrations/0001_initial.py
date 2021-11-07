# Generated by Django 3.2.9 on 2021-11-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cardTop', models.ImageField(blank=True, null=True, upload_to='photos/blog')),
                ('altDesc1', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=100, null=True)),
                ('excerpt', models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.', max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='photos/blog')),
                ('industry', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=50, null=True)),
                ('location', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=50, null=True)),
                ('goals', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=200, null=True)),
                ('type_of_business', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=100, null=True)),
                ('service1', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=100, null=True)),
                ('service2', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=100, null=True)),
                ('body1', models.TextField()),
                ('bodyImage1', models.ImageField(blank=True, null=True, upload_to='photos/stories')),
                ('altDesc2', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=100, null=True)),
                ('body2', models.TextField()),
                ('bodyImage2', models.ImageField(blank=True, null=True, upload_to='photos/stories')),
                ('altDesc3', models.CharField(blank=True, default='Lorem ipsum dolor sit amet', max_length=100, null=True)),
                ('body3', models.TextField()),
                ('quote', models.TextField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
