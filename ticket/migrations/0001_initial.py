# Generated by Django 4.2.7 on 2023-12-01 11:29

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField(null=True)),
                ('date_assigned', models.DateTimeField(null=True)),
                ('is_assigned', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Closed', 'Closed')], max_length=15)),
                ('is_resolved', models.BooleanField(default=False)),
                ('resolution_steps', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.category')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='engineer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
