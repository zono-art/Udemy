# Generated by Django 3.2.5 on 2021-07-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
