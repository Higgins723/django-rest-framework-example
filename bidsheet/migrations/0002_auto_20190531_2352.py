# Generated by Django 2.2 on 2019-05-31 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidsheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidsheet',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='bill_to',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='date_ordered',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='date_promised',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='grand_total',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='job_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='order_taken_by',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='total_for_extras',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bidsheet',
            name='total_materials_and_labor',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
