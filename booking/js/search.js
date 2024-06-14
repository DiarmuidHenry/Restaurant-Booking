// $(document).ready(function() {
//     $('#checkAvailabilityBtn').click(function() {
//         $.ajax({
//             type: "POST",
//             url: "{% url 'check_availability' %}",
//             data: $('#reservationForm').serialize(),
//             success: function(response) {
//                 $('#availabilityResult').html(response);
//             },
//             error: function(xhr, errmsg, err) {
//                 console.log(xhr.status + ": " + xhr.responseText);
//             }
//         });
//     });
// });