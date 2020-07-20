# Generated by Django 2.2.12 on 2020-07-16 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('grade', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('birth_date', models.DateField(verbose_name='date birth')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Classes')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='schools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Schools'),
        ),
    ]