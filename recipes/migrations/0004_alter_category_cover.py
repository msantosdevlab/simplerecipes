# Generated by Django 5.1.3 on 2024-11-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_servings_time_recipe_servings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.ImageField(null=True, upload_to='recipes/covers/%Y/%m/%d/'),
        ),
    ]
