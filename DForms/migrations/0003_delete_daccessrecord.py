# Generated by Django 4.2.1 on 2023-07-11 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DForms', '0002_daccessrecord_dsignup_dtopic_dwebpage_delete_signup_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DAccessRecord',
        ),
    ]