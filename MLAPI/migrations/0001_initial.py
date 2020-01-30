# Generated by Django 2.2.7 on 2020-01-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caller_id', models.IntegerField()),
                ('opened_by', models.IntegerField()),
                ('sys_mod_count', models.IntegerField()),
                ('category', models.IntegerField()),
                ('subcategory', models.IntegerField()),
                ('assigned_to', models.IntegerField()),
                ('assignment_group', models.IntegerField()),
                ('location', models.IntegerField()),
                ('opened_at_day', models.IntegerField()),
                ('opened_at_month', models.IntegerField()),
                ('opened_at_minute', models.IntegerField()),
                ('sys_updated_day', models.IntegerField()),
                ('sys_updated_month', models.IntegerField()),
                ('reassignment_count', models.IntegerField()),
            ],
        ),
    ]
