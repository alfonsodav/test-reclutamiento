# Generated by Django 3.2.5 on 2021-07-08 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20210707_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='Hotel',
            new_name='hotel',
        ),
        migrations.AddField(
            model_name='factura',
            name='metodo_pago',
            field=models.CharField(choices=[('TRANSFERENCIA', 'transferencia'), ('EFECTIVO', 'efectivo'), ('CHEQUE', 'cheque')], default=1, max_length=20, verbose_name='metodo de pago'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(auto_created=True, blank=True, default=datetime.date(2021, 7, 8), null=True),
        ),
    ]