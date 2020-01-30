

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MLAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='assigned_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='assignment_group',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='caller_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='category',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='location',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='opened_at_day',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='features',
            name='opened_at_month',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='features',
            name='opened_by',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='reassignment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='subcategory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='sys_mod_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='features',
            name='sys_updated_day',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(31), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='features',
            name='sys_updated_month',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
    ]
