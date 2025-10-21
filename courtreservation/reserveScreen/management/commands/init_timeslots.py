from django.core.management.base import BaseCommand
from reserveScreen.models import TimeSlot

class Command(BaseCommand):
    help = 'Initialize time slots for court reservations'

    def handle(self, *args, **kwargs):
        # Define time slots
        time_slots = [
            {'time': '8:00 AM', 'display_order': 1},
            {'time': '9:00 AM', 'display_order': 2},
            {'time': '10:00 AM', 'display_order': 3},
            {'time': '11:00 AM', 'display_order': 4},
            {'time': '12:00 PM', 'display_order': 5},
            {'time': '1:00 PM', 'display_order': 6},
            {'time': '2:00 PM', 'display_order': 7},
            {'time': '3:00 PM', 'display_order': 8},
            {'time': '4:00 PM', 'display_order': 9},
            {'time': '5:00 PM', 'display_order': 10},
            {'time': '6:00 PM', 'display_order': 11},
            {'time': '7:00 PM', 'display_order': 12},
        ]

        # Create time slots
        created_count = 0
        for slot_data in time_slots:
            slot, created = TimeSlot.objects.get_or_create(
                time=slot_data['time'],
                defaults={'display_order': slot_data['display_order']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created time slot: {slot.time}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Time slot already exists: {slot.time}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nTotal: {created_count} new time slots created')
        )
