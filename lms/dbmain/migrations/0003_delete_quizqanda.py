# Generated by Django 4.2.6 on 2023-10-19 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbmain', '0002_rename_fk_nstructor_classschedule_fk_instructor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuizQAndA',
        ),
    ]