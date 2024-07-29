import click

#varias formas de importar: from

from app.Model import Calculadora
@click.group()
@click.pass_context
def calc(ctx: click.Context):
    """A simple calculator"""
    ctx.obj = {"calculator_objetos": Calculadora()}