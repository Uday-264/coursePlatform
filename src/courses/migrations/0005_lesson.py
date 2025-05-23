# Generated by Django 5.1.8 on 2025-04-17 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('preview', models.BooleanField(default=False, help_text='if User doesnt have access to course,can they see this')),
                ('status', models.CharField(choices=[('publish', 'Published'), ('soon', 'Comming Soon'), ('draft', 'Draft')], default='publish', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
