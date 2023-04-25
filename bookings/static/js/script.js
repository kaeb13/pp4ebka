// Get a reference to the date input field and the time select field
const dateInput = document.querySelector('input[name="date"]');
const timeSelect = document.querySelector('select[name="time"]');

// Set up a listener for when the user selects a date
dateInput.addEventListener('change', () => {
  // Get the selected date
  const selectedDate = new Date(dateInput.value);

  // Make an AJAX request to get the available time slots for that date
  fetch(`/get_time_slots?date=${selectedDate.toISOString()}`)
    .then(response => response.json())
    .then(timeSlots => {
      // Clear the current options in the time select field
      timeSelect.innerHTML = '';

      // Add a new option for each available time slot
      timeSlots.forEach(timeSlot => {
        const option = document.createElement('option');
        option.value = timeSlot.time;
        option.textContent = timeSlot.display;
        timeSelect.appendChild(option);
      });
    })
    .catch(error => {
      console.error(error);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      events: '/bookings/api/events/',
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
      },
      selectable: true,
      selectMirror: true,
      select: function(arg) {
        var title = prompt('Event Title:');
        if (title) {
          calendar.addEvent({
            title: title,
            start: arg.start,
            end: arg.end,
            allDay: arg.allDay
          })
        }
        calendar.unselect()
      },
      eventClick: function(arg) {
        if (confirm('Are you sure you want to delete this event?')) {
          arg.event.remove()
        }
      }
    });
    calendar.render();
  });document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      events: '/bookings/api/events/',
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
      },
      selectable: true,
      selectMirror: true,
      select: function(arg) {
        var title = prompt('Event Title:');
        if (title) {
          calendar.addEvent({
            title: title,
            start: arg.start,
            end: arg.end,
            allDay: arg.allDay
          })
        }
        calendar.unselect()
      },
      eventClick: function(arg) {
        if (confirm('Are you sure you want to delete this event?')) {
          arg.event.remove()
        }
      }
    });
    calendar.render();
  });

  console.log("hello!");