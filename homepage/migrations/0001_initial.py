# Generated by Django 2.0.5 on 2018-06-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50)),
                ('pic1', models.ImageField(upload_to='./companyintro')),
                ('pic2', models.ImageField(upload_to='./companyintro')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='./homeBanner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='./product')),
            ],
        ),
        migrations.CreateModel(
            name='SuccessCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='./successcase')),
            ],
        ),
    ]
