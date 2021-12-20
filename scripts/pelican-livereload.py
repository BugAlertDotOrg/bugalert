#!/usr/bin/env python

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from livereload import Server, shell
from pelican import Pelican
from pelican.settings import read_settings


settings = read_settings('pelicanconf.py')
p = Pelican(settings)


def compile():
    try:
        p.run()
    except SystemExit as e:
        pass

server = Server()
server.watch(p.settings['PATH'], compile)
server.watch(p.settings['THEME'], compile)
server.watch('./pelicanconf.py', compile)

host_port = p.settings.get('SITEURL') or 'http://localhost:5500'
details = urlparse(host_port)
host, port = details[1].split(':')

server.serve(host=host, port=port, root=settings['OUTPUT_PATH'])
