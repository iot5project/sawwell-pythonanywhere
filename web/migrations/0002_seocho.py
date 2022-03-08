

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seocho',
            fields=[
                ('marketno', models.IntegerField(primary_key=True, serialize=False)),
                ('marketname', models.CharField(blank=True, max_length=50, null=True)),
                ('ceoname', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('categori', models.CharField(blank=True, max_length=100, null=True)),
                ('food', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'seocho',
            },
        ),
    ]
