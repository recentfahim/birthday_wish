from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed user model for development'

    def add_arguments(self, parser):
        parser.add_argument('--num', type=int, help='Number of user to seed')

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Start seeding user....')
        )
        num = options.get('--num', 10)
        for i in range(num):
            values = {
                'first_name': 'Test ' + str(i),
                'last_name': 'User ' + str(i),
                'email': 'test_user' + str(i) + '@gmail.com',
                'date_of_birth': timezone.now()
            }
            if i == 0:
                values['is_superuser'] = True
                values['is_staff'] = True

            user = User(**values)
            user.set_password('12345')
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully seed user for email: {values["email"]}')
            )

        self.stdout.write(
            self.style.SUCCESS('End seeding user....')
        )