# Generated by Django 3.0 on 2020-02-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('mobnumber', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=100)),
                ('classes', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=60)),
                ('repassword', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=20)),
                ('bday', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.RunSQL("insert into user (username,email,password) values('admin','admin@gmail.com','admin')")
    ]
