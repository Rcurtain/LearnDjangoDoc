# Generated by Django 2.1.3 on 2018-11-05 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_jioned', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeltest.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeltest.Group'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='modeltest.Membership', to='modeltest.Person'),
        ),
    ]
