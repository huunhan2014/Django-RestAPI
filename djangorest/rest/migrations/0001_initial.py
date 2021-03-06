# Generated by Django 2.2.12 on 2020-06-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('read_time', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
