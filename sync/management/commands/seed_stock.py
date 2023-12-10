from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker
import random
from faker import Faker
from sync.models import Stock, Items
import os
from django.core.files import File
from django.conf import settings


class Command(BaseCommand):
    help = "Users can use this command to generate stock item data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--stock",
            default=1,
            type=int,
            help="How many do you want Create Stock",
        )

    def generate_image(self):
        fake = Faker()
        image_content = fake.image()

        # 로컬에 파일 저장
        destination_path = settings.BASE_DIR
        file_name = "test_image.jpg"
        destination = os.path.join(destination_path, file_name)

        with open(destination, "wb") as f:
            f.write(image_content)

    def handle(self, *args, **options):
        stock = int(options.get("stock"))
        seeder = Seed.seeder()
        fake = Faker()

        items = Items.objects.all()
        # self.generate_image()

        seeder.add_entity(
            Stock,
            stock,
            {
                "item": lambda x: fake.random_element(items),
                "item_stock": lambda x: fake.random_int(min=1, max=100),
                "discontinued": False,
                "discontinued_at": None,
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{stock} dummy items has been created!"))
