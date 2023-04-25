const timeSelect = document.getElementById('id_time');
const instructorSelect = document.getElementById('id_instructor');
const workoutTypeSelect = document.getElementById('id_workout_type');
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

function updateAvailableTimeSlots() {
  const date = document.getElementById('id_date').value;
  const instructorId = instructorSelect.value;
  const workoutTypeId = workoutTypeSelect.value;
  const url = `/available_time_slots/${date}/?instructor=${instructorId}&workout_type=${workoutTypeId}`;
  
  fetch(url, {
    headers: {
      'X-CSRFToken': csrfToken
    }
  })
  .then(response => response.json())
  .then(data => {
    // Remove existing options from the time select element
    while (timeSelect.options.length > 1) {
      timeSelect.remove(1);
    }
    
    // Add new options for the available time slots
    data.available_slots.forEach(slot => {
      const option = document.createElement('option');
      option.value = slot;
      option.textContent = slot;
      timeSelect.add(option);
    });
  })
  .catch(error => console.error(error));
}

// Update available time slots when the date, instructor, or workout type changes
document.getElementById('id_date').addEventListener('change', updateAvailableTimeSlots);
instructorSelect.addEventListener('change', updateAvailableTimeSlots);
workoutTypeSelect.addEventListener('change', updateAvailableTimeSlots);

// Initial update of available time slots
updateAvailableTimeSlots();
