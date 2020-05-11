# Generated by Django 2.2.12 on 2020-05-07 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_shop_read_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='read_num',
        ),
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Shop')),
            ],
        ),
    ]