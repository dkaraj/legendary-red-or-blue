from django.core.management.base import BaseCommand, CommandParser
import importlib
from django.db import transaction


class Command(BaseCommand):
    help = 'Create Key Pair'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-a', '--all', default=False, action='store_true',
                            help='Add if all modules that generate data should be executed.')

    def handle(self, *args, **options):
        if options.get('atomic'):
            return self.handle_atomic(**options)
        self.perform(**options)

    @transaction.atomic
    def handle_atomic(self, **kwargs):
        self.perform(**kwargs)

    def perform(self, **options):

        modules = []
        all = options.get('all') or options.get('a')
        if options.get('properties') or all:
            modules.append(
                'dummy_data.generator.properties')
        if not modules:
            print('No data to be generated.')

        for module in modules:
            m = importlib.import_module(module)
            m.generate()