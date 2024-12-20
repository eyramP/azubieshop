# Generated by Django 4.1.7 on 2024-12-03 21:41

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
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="When the cart was created."
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="When the cart was last updated."
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        help_text="Owner of the cart.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Name of the category.",
                        max_length=100,
                        verbose_name="category name",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Description of the category.", null=True
                    ),
                ),
                (
                    "parent_category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Parent category for nested categories.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategories",
                        to="store.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Total amount for the order.",
                        max_digits=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("processing", "Processing"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("canceled", "Canceled"),
                        ],
                        default="pending",
                        help_text="Current status of the order.",
                        max_length=20,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="When the order was placed."
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="When the order was last updated."
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who placed the order.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="Name of the product.", max_length=255),
                ),
                (
                    "description",
                    models.TextField(help_text="Detailed description of the product."),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Price of the product.",
                        max_digits=10,
                    ),
                ),
                (
                    "stock",
                    models.PositiveIntegerField(help_text="Number of items in stock."),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="When the product was added."
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="When the product was last updated."
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="Category of the product.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="store.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="When the product was added to the wishlist.",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="The product in the wishlist.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlisted_by",
                        to="store.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who owns this wishlist.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.PositiveIntegerField(
                        help_text="Rating given to the product."
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, help_text="Optional review comment.", null=True
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="When the review was created."
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Product being reviewed.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="store.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="User who wrote the review.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Image file of the product.",
                        upload_to="product_images/",
                    ),
                ),
                (
                    "alt_text",
                    models.CharField(
                        blank=True,
                        help_text="Alternate text for the image (for accessibility).",
                        max_length=255,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="The product this image belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="store.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        help_text="Quantity of the product ordered."
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Price of the product at the time of order.",
                        max_digits=10,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        help_text="The order this item belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="store.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="The product ordered.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=1, help_text="Quantity of the product in the cart."
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        help_text="The cart this item belongs to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="store.cart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="The product added to the cart.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.product",
                    ),
                ),
            ],
        ),
    ]
