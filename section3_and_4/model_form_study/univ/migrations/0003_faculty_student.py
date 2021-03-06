# Generated by Django 3.1.1 on 2021-01-02 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('univ', '0002_auto_20210103_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='学部ID')),
                ('name', models.CharField(max_length=20, verbose_name='学部名')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='氏名')),
                ('email', models.EmailField(max_length=50, verbose_name='メールアドレス')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='univ.faculty', verbose_name='学部ID')),
            ],
        ),
    ]
