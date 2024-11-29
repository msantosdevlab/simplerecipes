"""
Configuração do aplicativo 'recipes' no Django.

Esta classe define a configuração do aplicativo, incluindo o nome do aplicativo e o tipo de campo de chave primária padrão a ser utilizado nos modelos do aplicativo.

Atributos:
    - `default_auto_field`: Define o tipo de campo de chave primária a ser usado nos modelos.
    - `name`: Define o nome do aplicativo, utilizado para a configuração do Django.
"""

from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
