#!/usr/bin/env python
import click
import time
@click.command()
def hello():
    localtime = time.asctime(time.localtime(time.time()))
    click.echo(f'Hi, the current time is:\n {localtime}')

if __name__ == '__main__':
    hello()
