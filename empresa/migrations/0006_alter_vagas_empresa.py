# Generated by Django 4.1.3 on 2022-11-08 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_rename_tecnologia_empresa_tecnologias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.empresa'),
        ),
    ]
