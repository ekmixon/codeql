# Regression test for a false-positive in 'Uninitialized Local'

def func():
    safe = 0
    safe = 1
    safe = 0

from module1 import *

def func2():
    os

def findPluginJars(dir):
    return filter(
        lambda y: y,
        (
            os.path.join(root, f)
            for root, _, files in os.walk(f'{dir}/plugins')
            for f in files
        ),
    )
