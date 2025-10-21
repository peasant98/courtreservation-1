from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from courts1.models import Loaded_Team
from reserveScreen.models import Court, TimeSlot, Reservation
import themethod as tm
import json
from courts1.views import finder
# Create your views here.
def testy(request):
    x = request.session['my_key']
    group_pk_used = int(x)
    print(group_pk_used)

    # you can do this method
    courter, my_assignedteam = tm.assigner(group_pk_used)

    if my_assignedteam != None:
        namer = str(my_assignedteam.team_name)
    else:
        namer = False
        #courter, my_assignedteam = tm.assigner(group_pk_used)

    courtnumber = int(my_assignedteam.court_id.courtNum)



    # need something here that tells what the group's team key is

    return render(request, 'reserver/courtsdisplay.html',{'teams':Loaded_Team.objects.all(), 'yo_team': namer, 'courtNum': courtnumber})

def reservation_grid(request):
    """
    View for the interactive court reservation grid
    Shows time slots, courts, and allows users to make reservations
    """
    # Get all courts
    courts = Court.objects.all().order_by('courtNum')

    # Get all time slots
    time_slots = TimeSlot.objects.all().order_by('display_order')

    # Get all reservations
    reservations = Reservation.objects.select_related('court', 'time_slot').all()

    # Build reservation data for template
    reservation_data = {}
    for res in reservations:
        key = f"{res.time_slot.id}-{res.court.id}"
        reservation_data[key] = {
            'reserved': res.is_reserved,
            'reserved_by': res.reserved_by if res.is_reserved else None
        }

    context = {
        'courts': courts,
        'time_slots': time_slots,
        'reservations_json': json.dumps(reservation_data)
    }

    return render(request, 'reserver/reservation_grid.html', context)

def make_reservation(request):
    """
    API endpoint to create a reservation
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            court_id = data.get('court_id')
            time_slot_id = data.get('time_slot_id')
            reserved_by = data.get('reserved_by')

            # Get or create reservation
            reservation, created = Reservation.objects.get_or_create(
                court_id=court_id,
                time_slot_id=time_slot_id,
                defaults={'reserved_by': reserved_by, 'is_reserved': True}
            )

            if not created and not reservation.is_reserved:
                # Update existing reservation
                reservation.reserved_by = reserved_by
                reservation.is_reserved = True
                reservation.save()

            return JsonResponse({
                'success': True,
                'message': 'Reservation created successfully'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)
