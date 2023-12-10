from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from faker import Faker
from django.contrib.auth.models import User
from sync.models import UserOrder, Items


class Command(BaseCommand):
    help = "Users can use this command to generate user order item data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--userorder",
            default=1,
            type=int,
            help="How many do you want Create User Order",
        )

    def handle(self, *args, **options):
        user_orders = int(options.get("userorder"))
        seeder = Seed.seeder()
        fake = Faker()

        items = Items.objects.all()
        users = User.objects.all()
        # 더미 유저를 만들어주는 코드 {} 안에 들어가는 값은 랜덤하지 않은 내용을 넣고싶을때 넣어주는 부분
        seeder.add_entity(
            UserOrder,
            user_orders,
            {
                "item": lambda x: fake.random_element(items),
                "user": lambda x: fake.random_element(users),
                "order_quantity": lambda x: fake.random_int(min=1, max=100),
                "address": lambda x: fake.address(),
            },
        )
        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"{user_orders} dummy items has been created!")
        )
