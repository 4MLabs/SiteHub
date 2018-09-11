from __future__ import unicode_literals

import multiprocessing
import argparse

import gunicorn.app.base

from gunicorn.six import iteritems
from sites_hub.wsgi import application

from django.core import management


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class SitesHubApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(SitesHubApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8000'),
        'workers': number_of_workers(),
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--setup", action='store_true',
                        help="Setup SitesHub")

    parser.add_argument("-r", "--run", action='store_true',
                        help="Start SitesHub WebServer")

    parser.add_argument("--collectstatic", action='store_true',
                        help="Perform collectstatic")

    parser.add_argument("--createsuperuser", action='store_true',
                        help="Create superuser")

    parser.add_argument("--cleardb", action='store_true',
                        help="Clear Database")

    parser.add_argument("--flushdb", action='store_true',
                        help="Flush Database")

    args = parser.parse_args()

    if args.setup:
        management.call_command('makemigrations')
        management.call_command('migrate')
        management.call_command('collectstatic')
        management.call_command('createsuperuser')

    if args.collectstatic:
        management.call_command('collectstatic')

    if args.createsuperuser:
        management.call_command('createsuperuser')

    if args.cleardb:
        management.call_command('sqlflush')

    if args.cleardb:
        management.call_command('flush')

    if args.run:
        SitesHubApplication(application, options).run()


