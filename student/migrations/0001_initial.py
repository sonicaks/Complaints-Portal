# Generated by Django 3.0.4 on 2020-03-22 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('message_html', models.TextField(editable=False)),
                ('type', models.CharField(choices=[('ELE', 'Electrical'), ('PLU', 'Plumbing'), ('GLA', 'Glass'), ('CAR', 'Wood')], max_length=3)),
                ('hall', models.CharField(choices=[('MV', 'MV Hall'), ('GDB', 'GDB Hall'), ('DBA', 'DBA Hall'), ('MSS', 'MSS Hall'), ('VS', 'VS Hall'), ('SD', 'SD Hall'), ('HB', 'HB Hall'), ('SSB', 'SSB Hall'), ('KMS', 'KMS Hall'), ('CVR', 'CVR Hall')], max_length=3)),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('PRO', 'In progress'), ('COM', 'Finished')], default='PEN', max_length=3)),
                ('block_number', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('room_number', models.CharField(max_length=3)),
                ('roll_number', models.CharField(max_length=9)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
