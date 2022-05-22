# Generated by Django 4.0.4 on 2022-05-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('admission_number', models.IntegerField(unique=True)),
                ('is_qualified', models.BooleanField(default=False)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('student_capacity', models.IntegerField()),
                ('students', models.ManyToManyField(to='schoolapp.student')),
            ],
        ),
    ]
