# Generated by Django 4.1.4 on 2022-12-12 16:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ligue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ligue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_participant', models.CharField(max_length=200)),
                ('prenom_participant', models.CharField(max_length=200)),
                ('ligue', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tennis.ligue')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_match', models.CharField(max_length=200)),
                ('date_match', models.DateField(default=datetime.date.today)),
                ('score', models.IntegerField()),
                ('participant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tennis.participant')),
            ],
        ),
    ]