# Generated by Django 3.2 on 2022-11-12 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_productagewiselist'),
    ]

    operations = [
        migrations.AddField(
            model_name='productagewiselist',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productagewiselist',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.productmaster'),
        ),
    ]
