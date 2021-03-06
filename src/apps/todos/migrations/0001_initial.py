# Generated by Django 2.2.6 on 2019-10-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', verbose_name='title')),
                ('due_date', models.DateField(verbose_name='due date')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'In queue'), (1, 'Later'), (2, 'Done')], default=0, verbose_name='status')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
            },
        ),
    ]
