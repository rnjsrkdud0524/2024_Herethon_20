# Generated by Django 4.2.11 on 2024-07-03 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homst', '0003_searchrecord_travel_date2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('safety_filters', models.ManyToManyField(to='homst.safetyfilter')),
            ],
        ),
    ]
