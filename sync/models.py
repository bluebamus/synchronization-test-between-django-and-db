from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=20)
    item_group = models.CharField(max_length=10)
    item_number = models.IntegerField()
    item_expiration = models.DateTimeField(blank=True, null=True)
    default_order_stock = models.IntegerField(default=30)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "items"
        unique_together = (("item_name", "item_number"),)
        indexes = [
            models.Index(fields=["item_expiration"], name="item_expiration_idx"),
        ]
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.item_name


class UserOrder(models.Model):
    order_quantity = models.IntegerField()
    item = models.ForeignKey(Items, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    address = models.CharField(blank=True, null=True, max_length=200)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "user_order"
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"{self.item.item_name}-{self.user.username}"


class Stock(models.Model):
    item = models.ForeignKey(Items, models.DO_NOTHING)
    item_stock = models.IntegerField(default=0)
    discontinued = models.BooleanField(default=False)
    discontinued_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "stock"
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.item.item_name


class StockOrder(models.Model):
    item = models.ForeignKey(Items, models.DO_NOTHING)
    admin = models.ForeignKey(User, models.DO_NOTHING)
    order_quantity = models.IntegerField()
    ordered_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    estimated_arrival_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "stock_order"
        ordering = [
            "-ordered_at",
        ]

    def __str__(self):
        return self.item.item_name


class ItemCodeInOrder(models.Model):
    item_name = models.CharField(max_length=20, blank=True, null=True)
    item_full_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "item_code_in_order"


class FullInfoForStockOrder(models.Model):
    item_name = models.CharField(max_length=20, blank=True, null=True)
    item_full_code = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "full_info_for_stock_order"
