# -*- coding: utf-8 -*-

import os
from invoke import task

root = os.path.dirname(os.path.abspath(__file__))
name = 'Card'


@task
def clean(ctx):
    ctx.run('rm -rf build dist', echo=True)
    ctx.run("find . -name '*.pyc' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '*.pyo' -exec rm -f {} +", echo=True)
    ctx.run("find . -name '__pycache__' -exec rm -rf {} +", echo=True)


@task(clean)
def build(ctx):
    build_dir = os.path.join(root, 'build')
    ctx.run('mkdir -p {build_dir}'.format(build_dir=build_dir), echo=True)
    include_dir = [
        os.path.join(root, name)
    ]
    ctx.run('cp -r {dirs} {build_dir}'.format(dirs=' '.join(include_dir), build_dir=build_dir), echo=True)

@task
def lock(ctx):
    ctx.run(
        "pipenv lock -v --keep-outdated", echo=True
    )
