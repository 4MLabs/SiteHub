from __future__ import unicode_literals

import multiprocessing

import gunicorn.app.base

from gunicorn.six import iteritems
from sites_hub.wsgi import application


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
    SitesHubApplication(application, options).run()
