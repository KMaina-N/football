# Generated by Django 4.2.7 on 2023-11-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_city', models.CharField(max_length=200)),
                ('win', models.BooleanField(default=False)),
            ],
        ),
    ]