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
            $.each(available_slots, function(index, slot) {
                timeField.append(`<option value="${slot[1]}">${slot[0]}</option>`);
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


document.addEventListener("DOMContentLoaded", function () {
    const bookingForm = document.getElementById("booking-form");
  
    bookingForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(bookingForm);
  
      fetch(bookingForm.action, {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
        },
      })
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Form submission failed.");
          }
        })
        .then((data) => {
          if (data && data.booking_id) {
            window.location.href = `/confirm_booking/${data.booking_id}/`;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });