"""
Este módulo define os modelos para o aplicativo de receitas.

Classes:
    Category: Representa uma categoria de receitas, como "Sobremesas" ou "Massas".
    Recipe: Representa uma receita com informações detalhadas, como título,
            descrição, tempo de preparo, etc.
"""

from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    """
    Representa uma categoria de receitas.

    Attributes:
        name (CharField): O nome da categoria (ex.: "Sobremesas").
        cover (ImageField): Uma imagem de capa para a categoria.
    """
    name = models.CharField(max_length=65)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', null=True, blank=False)

    def __str__(self):  # pylint: disable=E0307
        """
        Retorna uma representação em string da categoria.

        Returns:
            str: O nome da categoria.
        """
        return str(self.name)


class Recipe(models.Model):
    """
    Representa uma receita com informações detalhadas.

    Attributes:
        title (CharField): O título da receita.
        description (CharField): Uma breve descrição da receita.
        slug (SlugField): Um identificador único para a receita (usado em URLs).
        preparation_time (IntegerField): O tempo de preparo em unidades específicas.
        preparation_time_unit (CharField): A unidade de tempo (ex.: "minutos").
        servings (IntegerField): O número de porções que a receita rende.
        servings_unit (CharField): A unidade de porções (ex.: "pessoas").
        preparation_steps (TextField): O passo a passo para preparar a receita.
        preparation_steps_is_html (BooleanField): Indica se os passos estão formatados em HTML.
        created_at (DateTimeField): A data e hora em que a receita foi criada.
        updated_at (DateTimeField): A data e hora da última atualização da receita.
        is_published (BooleanField): Indica se a receita está publicada.
        cover (ImageField): Uma imagem de capa para a receita.
        category (ForeignKey): A categoria associada à receita.
        author (ForeignKey): O autor da receita (usuário do sistema).
    """
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=365)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, null=True, default=9)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self)  -> str:
        """
        Retorna uma representação em string da receita.

        Returns:
            str: O título da receita.
        """
        return str(self.title)
