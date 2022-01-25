# Generated by Django 3.1.4 on 2020-12-03 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('photo_url', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album', models.CharField(default='no album provided', max_length=100)),
                ('preview_url', models.TextField(blank=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='tunr.artist')),
            ],
        ),
    ]