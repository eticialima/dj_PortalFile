# Generated by Django 3.2.5 on 2021-10-13 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type_user',
            field=models.CharField(choices=[('ad', 'Administrador'), ('co', 'Colaborador'), ('us', 'Usuario Padrão')], max_length=2, verbose_name='type_user'),
        ),
    ]
