from django.db import models


class Profile(models.Model):
    """Наследуемся от базовой модели User которую предоставляет Django"""

    telegram_id = models.IntegerField(primary_key=True)
    telegram_username = models.CharField(max_length=64, null=True)
    balance = models.IntegerField("Баланс", default=0)

    class Meta:
        db_table = "user_profile"

    def __str__(self) -> str:
        return f"{self.telegram_id} {self.balance}"


class UserPurchase(models.Model):
    owner = models.ForeignKey(
        Profile, related_name="purchases", on_delete=models.CASCADE
    )
    product_title = models.CharField(max_length=128)
    product_image = models.CharField(max_length=256, null=True)
    product_description = models.CharField(max_length=512, null=True)
    product_price = models.IntegerField(default=100)

    class Meta:
        db_table = "user_purchase"

    def __str__(self) -> str:
        return f"{self.owner.telegram_username} {self.product_title}"


class UserProductOnSale(models.Model):
    owner = models.ForeignKey(Profile, related_name="onsales", on_delete=models.CASCADE)
    product_title = models.CharField(max_length=128)
    product_image = models.CharField(max_length=256, null=True)
    product_description = models.CharField(max_length=512, null=True)
    product_price = models.IntegerField(default=100)

    class Meta:
        db_table = "user_sales"

    def __str__(self) -> str:
        return f"{self.owner.telegram_username} {self.product_title}"
