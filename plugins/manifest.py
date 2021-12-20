import json
import logging
import os
import time

from pelican.generators import Generator
from pelican import signals


logger = logging.getLogger(__name__)


class ManifestGenerator(Generator):

    def generate_context(self):
        self.file_name = os.path.join(self.output_path, 'manifest.json')

    def generate_output(self, writer):
        logger.info('Generating manifest.json...')

        data = self._create_manifest_data()
        with open(self.file_name, 'w') as manifest:
            manifest.write(json.dumps(data, indent=4))

    def _create_url(self, relative_url):
        return '%s/%s' % (self.settings.get('SITEURL', ''), relative_url)

    def _convert_wrapper(self, obj):

        return {
            'name': obj.name,
            'slug': obj.slug,
            'url': self._create_url(obj.url)
        }

    def _iter_articles(self):
        for article in self.context.get('articles', tuple()):
            result = {
                'title': article.title,
                'summary': article.summary,
                'category': self._convert_wrapper(article.category),
                'date': time.mktime(article.date.timetuple()),
                'uri': self._create_url(article.url),
                'author': self._convert_wrapper(article.author),
                'email': article.metadata.get('email', None),
            }

            tags = getattr(article, 'tags', [])
            result['tags'] = tuple(self._convert_wrapper(tag) for tag in tags)
            yield result

    def _create_manifest_data(self):
        return tuple(self._iter_articles())


def get_manifest_generator(pelican_object):
    # define a new generator here if you need to
    return ManifestGenerator


def register():
    signals.get_generators.connect(get_manifest_generator)
