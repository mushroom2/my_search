import logging
from django.core.management.base import BaseCommand
import urllib3
import tarfile
import os


class Command(BaseCommand):

    help = 'download universal-sentence-encoder from TensorFlowHub'

    logger = logging.getLogger(f'{__name__}.Command')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        self.logger.info(f'Download started')
        http = urllib3.PoolManager()
        r = http.request('GET', 'https://tfhub.dev/google/universal-sentence-encoder/2?tf-hub-format=compressed')
        with open('textes/data/encoder.tar.gz', 'wb') as f:
            f.write(r.data)
        self.logger.info(f'Download finished')
        self.logger.info(f'Extracting..')
        with tarfile.open('textes/data/encoder.tar.gz') as tar:
            tar.extractall('textes/data/')
        os.remove('textes/data/encoder.tar.gz')
        self.logger.info(f'OK.')


