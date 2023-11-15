# Generated by Django 4.2.6 on 2023-11-14 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='img/no_avatar.jpeg', upload_to='static/avatar/%y/%m/%d', verbose_name='Аватар')),
                ('user_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32, unique=True, verbose_name='Тег')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('number_of_answers', models.IntegerField(default=0, verbose_name='Количество ответов')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('dislikes', models.IntegerField(default=0, verbose_name='Дизлайки')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Автор')),
                ('tags', models.ManyToManyField(to='app.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст ответа')),
                ('correctness', models.BooleanField(default=False, verbose_name='Корректность ответа')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('dislikes', models.IntegerField(default=0, verbose_name='Дизлайки')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Автор')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='LikeQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=True, verbose_name='Реакция')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Профиль')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Лайк вопроса',
                'verbose_name_plural': 'Лайки вопросов',
                'unique_together': {('question_id', 'profile_id')},
            },
        ),
        migrations.CreateModel(
            name='LikeAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=True, verbose_name='Реакция')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.answer', verbose_name='Ответ')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Лайк ответа',
                'verbose_name_plural': 'Лайки ответов',
                'unique_together': {('answer_id', 'profile_id')},
            },
        ),
    ]
