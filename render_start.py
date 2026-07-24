"""
Ponto de entrada para o Render.
Sobe o Flask com Gunicorn E o bot Discord simultaneamente.
"""
import os
import sys

# Importa o bot (que já tem a lógica de Flask + bot)
import bot
