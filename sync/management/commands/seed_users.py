from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django_seed import Seed
from faker import Faker
import random


class Command(BaseCommand):
    help = "Users can create a random user using this command."

    def add_arguments(self, parser):
        parser.add_argument(
            "--users",
            default=1,
            type=int,
            help="How many do you want Create User",
        )

    def handle(self, *args, **options):
        users = int(options.get("users"))
        seeder = Seed.seeder()
        # 더미 유저를 만들어주는 코드 {} 안에 들어가는 값은 랜덤하지 않은 내용을 넣고싶을때 넣어주는 부분
        seeder.add_entity(
            User,
            users,
            {
                "username": lambda x: Faker().name(),
                "email": lambda x: seeder.faker.email(),
                "password": lambda x: Faker().password(),
                "is_active": True,
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{users} dummy users has been created!"))
