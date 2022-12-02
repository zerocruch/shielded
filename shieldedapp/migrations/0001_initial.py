# Generated by Django 3.2.12 on 2022-12-01 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=255, unique=True)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Password', models.CharField(max_length=255)),
                ('Role', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField(max_length=10240)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('By', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shieldedapp.users')),
            ],
        ),
    ]
