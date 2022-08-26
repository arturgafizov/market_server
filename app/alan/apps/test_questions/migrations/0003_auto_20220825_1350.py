# Generated by Django 3.2.12 on 2022-08-25 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
        ('test_questions', '0002_alter_testquestion_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testanswer',
            old_name='test_question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='testquestionanswer',
            old_name='test_answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='testquestionanswer',
            old_name='test_questions',
            new_name='questions',
        ),
        migrations.AddField(
            model_name='testresult',
            name='questions',
            field=models.ManyToManyField(related_name='question_set', to='test_questions.TestQuestion', verbose_name='вопросы'),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_set', to='docs.category'),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.speciality', verbose_name='Специальность'),
        ),
    ]