# Generated by Django 2.0.4 on 2018-05-06 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sems.Programs'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sems.Courses'),
        ),
    ]