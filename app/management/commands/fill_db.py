from django.core.management.base import BaseCommand
from app.models import Profile, Question, Tag, Answer, LikeAnswer, LikeQuestion
from django.contrib.auth.models import User
from random import choice, sample, randint
from faker import Faker
from django.db import IntegrityError

f = Faker()

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Specify the ratio for data creation')

        parser.add_argument('--auto', nargs='+', type=int)
        parser.add_argument('--users', nargs='+', type=int)
        parser.add_argument('--questions', nargs='+', type=int)
        parser.add_argument('--answers', nargs='+', type=int)
        parser.add_argument('--tags', nargs='+', type=int)
        parser.add_argument('--likes', nargs='+', type=int)
        parser.add_argument('--db_size', nargs='+', type=str)

    def handle(self, *args, **options):
        ratio = options['ratio']
        
        if options['auto']:
            self.fill_db(options['auto'][0])
        else:
            self.fill_db(ratio)

        if options['users']:
            self.fill_profile(options['users'][0])

        if options['tags']:
            self.fill_tag(options['tags'][0])

        if options['questions']:
            self.fill_questions(options['questions'][0])

        if options['answers']:
            self.fill_answers(options['answers'][0])

        if options['likes']:
            self.fill_likes_questions(options['likes'][0])
            self.fill_likes_answers(5 * options['likes'][0])

        self.stdout.write(self.style.SUCCESS('Data creation was successful'))


    @staticmethod
    def fill_profile(n):
        for i in range(n):
            username = f.user_name() + str(i)
            Profile.objects.create(
                user_id=User.objects.create_user(
                    username=username,
                    email=f.email(),
                    password="1"
                ),
                avatar="static/img/pic_" + str(i % 4) + ".jpg",
            )

    @staticmethod
    def fill_tag(n):
        for i in range(n):
            tag = f.word()
            attempts = 0
            max_attempts = 100  # You can adjust this number based on your needs

            while attempts < max_attempts:
                try:
                    Tag.objects.create(tag=tag)
                    break  # Break out of the loop if the tag is successfully created
                except IntegrityError:
                    # Handle the IntegrityError (tag already exists) by generating a new tag
                    tag = f.word()
                    attempts += 1

            if attempts >= max_attempts:
                # If we can't find a unique tag in a reasonable number of attempts, break the loop
                break
    
    @staticmethod
    def fill_questions(n):
        for profile in Profile.objects.all():
            q = Question.objects.create(
                profile_id=profile,
                title=f.sentence(),
                text=f.text(),
            )

            tag_ids = list(
                Tag.objects.values_list(
                    'tag', flat=True
                )
            )
            tags_list = sample(tag_ids, k=randint(1, 3))
            q.tags.set(Tag.objects.create_question(tags_list))
    
    @staticmethod
    def fill_answers(n):
        profile_ids = list(
            Profile.objects.values_list(
                'id', flat=True
            )
        )
        question_ids = list(
            Question.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(n):
            Answer.objects.create(
                profile_id=Profile.objects.get(pk=choice(profile_ids)),
                question_id=Question.objects.get(pk=choice(question_ids)),
                text=f.text(),
                correctness=f.random_int(min=0, max=1),
            )

    @staticmethod
    def fill_likes_questions(n):
        count = 0
        for question in Question.objects.all():
            for profile in Profile.objects.sample_profile(f.random_int(min=0, max=10)):
                LikeQuestion.objects.create(
                    question_id=question,
                    profile_id=profile,
                    is_like=f.random_int(min=0, max=1),
                )
                count += 1
                if count == n:
                    break
            if count == n:
                break

    @staticmethod
    def fill_likes_answers(n):
        count = 0
        for answer in Answer.objects.all():
            for profile in Profile.objects.sample_profile(f.random_int(min=0, max=15)):
                LikeAnswer.objects.create(
                    answer_id=answer,
                    profile_id=profile,
                    is_like=f.random_int(min=0, max=1),
                )
                count += 1
                if count == n:
                    break
            if count == n:
                break

    def fill_db(self, n):
        self.fill_profile(n)
        self.fill_tag(n)
        self.fill_questions(10 * n)
        self.fill_answers(100 * n)
        self.fill_likes_questions(200 * n)
        self.fill_likes_answers(200 * n)