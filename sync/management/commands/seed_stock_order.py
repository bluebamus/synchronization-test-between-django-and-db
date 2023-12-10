from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker
import random
from faker import Faker
from django.contrib.auth.models import User
from sync.models import StockOrder, Items


class Command(BaseCommand):
    help = "Users can use this command to generate user stock order data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--stockorder",
            default=1,
            type=int,
            help="How many do you want Create Stock Order",
        )

    def handle(self, *args, **options):
        stock_order = int(options.get("stockorder"))
        seeder = Seed.seeder()
        fake = Faker()

        items = Items.objects.all()
        users = User.objects.all()
        seeder.add_entity(
            StockOrder,
            stock_order,
            {
                "item": lambda x: fake.random_element(items),
                "admin": lambda x: fake.random_element(users),
                "order_quantity": lambda x: fake.random_int(min=1, max=100),
            },
        )
        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"{stock_order} dummy items has been created!")
        )
