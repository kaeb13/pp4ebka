$(document).ready(function() {
  let dateField = $('input[name="date"]');
  let timeField = $('select[name="time"]');
  let instructorField = $('select[name="instructor"]');
  let workoutTypeField = $('select[name="workout_type"]');

  function updateAvailableTimeSlots() {
    let instructor_id = instructorField.val();
    let workout_type_id = workoutTypeField.val();
    let date = dateField.val();

    if (instructor_id && workout_type_id && date) {
        let url = `/available_time_slots/${date}/?instructor=${instructor_id}&workout_type=${workout_type_id}`;
        $.getJSON(url, function(data) {
            let available_slots = data.available_slots;
            timeField.empty();
            timeField.append('<option value="" selected disabled>Select a time</option>');
            $.each(available_slots, function(index, time) {
                timeField.append('<option value="' + time + '">' + time + '</option>');
            });
        });
    } else {
        timeField.empty();
        timeField.append('<option value="" selected disabled>Select a time</option>');
    }
}

  instructorField.on('change', updateAvailableTimeSlots);
  workoutTypeField.on('change', updateAvailableTimeSlots);
  dateField.on('change', updateAvailableTimeSlots);
});
console.log("jQuery and script.js are connected!");