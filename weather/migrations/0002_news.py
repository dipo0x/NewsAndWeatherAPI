# Generated by Django 3.2.8 on 2021-10-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(blank=True, default='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
