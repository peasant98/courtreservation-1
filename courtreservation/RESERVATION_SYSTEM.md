# Court Reservation System

## Overview
This is an interactive court reservation system that allows users to view court availability across different time slots and make reservations.

## Features

### 1. Interactive Time Slot Selection
- View all available time slots (8:00 AM - 7:00 PM)
- Click on any time slot to see court availability
- Selected time slot is highlighted in purple

### 2. Court Availability Display
- See all courts for the selected time slot
- Available courts are highlighted in green
- Reserved courts are shown in red with reservation details
- Click on available courts to make a reservation

### 3. Full Schedule Sidebar
- View complete daily schedule
- See all time slots with court availability at a glance
- Color-coded status indicators for quick reference

### 4. Reservation Management
- Easy one-click reservation process
- Enter your name to complete a reservation
- View who has reserved each court

## Technical Implementation

### Models Added

#### TimeSlot
```python
- time: CharField - The time (e.g., "9:00 AM")
- display_order: IntegerField - For ordering time slots
```

#### Reservation
```python
- court: ForeignKey(Court) - The court being reserved
- time_slot: ForeignKey(TimeSlot) - The time slot
- reserved_by: CharField - Name of person who reserved
- is_reserved: BooleanField - Reservation status
```

### Views

#### reservation_grid
Main view that displays the interactive reservation grid.
- URL: `/reserver/reservation/`
- Template: `reserver/reservation_grid.html`
- Shows all courts, time slots, and current reservations

#### make_reservation
API endpoint for creating reservations.
- URL: `/reserver/api/reserve/`
- Method: POST
- Accepts JSON with court_id, time_slot_id, and reserved_by

### Templates
- `reservation_grid.html` - Interactive UI with JavaScript for real-time updates

## Setup Instructions

### 1. Run Database Migrations
```bash
python manage.py makemigrations reserveScreen
python manage.py migrate
```

### 2. Initialize Time Slots
```bash
python manage.py init_timeslots
```

This creates the default time slots from 8:00 AM to 7:00 PM.

### 3. Create Courts (if not already created)
You can create courts through the Django admin panel:
```bash
python manage.py createsuperuser  # if you haven't already
python manage.py runserver
```

Then go to `http://localhost:8000/admin/` and create Court objects.

### 4. Access the Reservation System
Navigate to: `http://localhost:8000/reserver/reservation/`

## Usage

1. **View Courts**: Open the reservation page to see all time slots
2. **Select Time**: Click on a time slot to view court availability
3. **Make Reservation**: Click on an available (green) court
4. **Enter Name**: Provide your name when prompted
5. **Confirm**: Your reservation is complete!

## File Structure
```
reserveScreen/
├── models.py                          # Updated with TimeSlot and Reservation
├── views.py                           # reservation_grid and make_reservation views
├── urls.py                            # URL routing
├── admin.py                           # Admin panel registration
├── templates/
│   └── reserver/
│       └── reservation_grid.html      # Main UI template
└── management/
    └── commands/
        └── init_timeslots.py          # Command to initialize time slots
```

## UI Features

### Color Coding
- **Purple**: Selected time slot
- **Green**: Available court
- **Red**: Reserved court
- **Light backgrounds**: Visual grouping

### Responsive Design
- Works on desktop and mobile devices
- Grid layout adapts to screen size
- Sidebar moves below on smaller screens

### Interactive Elements
- Hover effects on clickable items
- Smooth transitions and animations
- Clear visual feedback for user actions

## Future Enhancements
- User authentication for reservations
- Email notifications
- Cancellation functionality
- Recurring reservations
- Multi-day calendar view
- Real-time updates using WebSockets
- Payment integration
- Reservation time limits

## Troubleshooting

### No Time Slots Showing
Run the initialization command:
```bash
python manage.py init_timeslots
```

### No Courts Available
Create courts in the admin panel or run:
```python
from reserveScreen.models import Court
for i in range(1, 5):
    Court.objects.get_or_create(courtNum=i)
```

### Database Errors
Ensure migrations are up to date:
```bash
python manage.py migrate
```

## API Documentation

### POST /reserver/api/reserve/
Create a new reservation

**Request Body:**
```json
{
  "court_id": 1,
  "time_slot_id": 3,
  "reserved_by": "John Doe"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Reservation created successfully"
}
```

## Notes
- The current implementation uses sample data in the JavaScript
- To persist reservations, ensure the database is properly configured
- Django 1.9.12 has compatibility issues with Python 3.10+
- Consider upgrading Django for production use
