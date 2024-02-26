# Generated by Django 4.1.5 on 2023-01-21 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='school.student')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='school.teacher')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]