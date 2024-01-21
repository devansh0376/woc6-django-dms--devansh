# Generated by Django 4.2.5 on 2024-01-18 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('domain', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('Local', 'Local'), ('National', 'National'), ('International', 'International'), ('Regional', 'Regional')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('reported', 'reported'), ('in_progress', 'in_progress'), ('solved', 'solved')], default='reported', max_length=50)),
                ('report_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=2056, null=True)),
                ('severity_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol_name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('skills', models.CharField(choices=[('Time Management', 'Time Management'), ('Fire Safety', 'Fire Safety'), ('Physical Fitness', 'Physical Fitness'), ('Strength', 'Strength'), ('First Aid', 'First Aid')], max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('org_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DmsApp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('ward', models.IntegerField()),
                ('org_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DmsApp.organization')),
            ],
        ),
    ]