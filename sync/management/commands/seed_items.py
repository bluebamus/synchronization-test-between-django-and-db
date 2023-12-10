from django.core.management.base import BaseCommand
from sync.models import Items
from django_seed import Seed
from faker import Faker
import random
import uuid


class Command(BaseCommand):
    help = "Users can create random item data using this command."

    def add_arguments(self, parser):
        parser.add_argument(
            "--items",
            default=1,
            type=int,
            help="How many do you want Create Item",
        )

    def generate_10_digit_uuid(self):
        uuid_value = uuid.uuid4().hex

        short_uuid = uuid_value[:10]
        print("short_uuid : ", short_uuid)
        return short_uuid

    def handle(self, *args, **options):
        items_nb = int(options.get("items"))
        seeder = Seed.seeder()
        fake = Faker()

        seeder.add_entity(
            Items,
            items_nb,
            {
                "item_name": lambda x: fake.word(),
                "item_group": lambda x: self.generate_10_digit_uuid(),
                "item_number": lambda x: fake.random_int(min=100, max=1000),
                "default_order_stock": lambda x: fake.random_int(min=30, max=1000),
            },
        )
        seeder.execute()

        self.stdout.write(
            self.style.SUCCESS(f"{items_nb} dummy items has been created!")
        )
