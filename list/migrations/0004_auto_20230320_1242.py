# Generated by Django 3.2.18 on 2023-03-20 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20230311_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-added_on', '-star']},
        ),
        migrations.AlterField(
            model_name='note',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='list.entry'),
        ),
    ]
