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
        if not os.path.exists('textes/data'):
            os.mkdir('textes/data')
        self.logger.info(f'Download started')
        http = urllib3.PoolManager()
        r = http.request('GET', 'https://tfhub.dev/google/universal-sentence-encoder/2?tf-hub-format=compressed')
        with open('textes/data/encoder.tar.gz', 'wb') as f:
            f.write(r.data)
        self.logger.info(f'Download finished')
        self.logger.info(f'Extracting..')
        with tarfile.open('textes/data/encoder.tar.gz') as tar:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar, "textes/data/")
        os.remove('textes/data/encoder.tar.gz')
        self.logger.info(f'OK.')


