// console.log("Javascript file located and loaded")
// document.addEventListener('DOMContentLoaded', function () {
//     const reservationDateField = document.getElementById('id_reservation_date');
//     const reservationLengthField = document.getElementById('id_reservation_length');
//     const reservationTimeField = document.getElementById('id_reservation_time');
//     const reservationForm = document.getElementById('reservation_form');

//     function changeReservationInput() {
//         const selectedDate = reservationDateField.value;
//         const reservationLength = reservationLengthField.value;

//         if (selectedDate) {
//             fetchOpeningHours(selectedDate, reservationLength);
//         } else {
//             clearTimeOptions();
//         }
//     };

//     function fetchOpeningHours(date, length) {
//         console.log(`Fetching opening hours for date: ${date}`);
//         fetch(`/booking/reservation/get_opening_hours/?date=${date}`)
//             .then(response => response.json())
//             .then(data => {
//                 console.log('Received data:', data);
//                 if (data.error) {
//                     console.error(data.error);
//                     clearTimeOptions();
//                 } else {
//                     populateTimeOptions(data.opening_time, data.closing_time, length);
//                 }
//             })
//             .catch(error => {
//                 console.error('Error fetching opening hours:', error);
//                 clearTimeOptions();
//             });
//     }

//     function populateTimeOptions(openingTime, closingTime, length) {
//         if (openingTime === "00:00" && closingTime === "00:00") {
//             console.log("CLOSED")
//             reservationTimeField.innerHTML = null;
//         } else {
//             console.log(`Populating time options from ${openingTime} to ${length} hours before ${closingTime}`);
//             const reservationLength = length;
//             const [openingHour, openingMinute] = openingTime.split(':').map(Number);
//             const [closingHour, closingMinute] = closingTime.split(':').map(Number);

//             const times = [];
//             let currentHour = openingHour;
//             let currentMinute = openingMinute;

//             while ((currentHour < closingHour) || (currentHour === closingHour && currentMinute <= closingMinute)) {
//                 var reservationEndHour = currentHour + Math.floor(reservationLength);
//                 var reservationEndMinute = currentMinute + (reservationLength % 1) * 60;
//                 if (reservationEndMinute >= 60) {
//                     reservationEndHour += 1;
//                     reservationEndMinute -= 60;
//                 }

//                 if (reservationEndHour < closingHour || (reservationEndHour === closingHour && reservationEndMinute <= closingMinute)) {
//                     const formattedTime = `${String(currentHour).padStart(2, '0')}:${String(currentMinute).padStart(2, '0')}`;
//                     times.push(formattedTime);
//                 }
//                 currentMinute += 15;
//                 if (currentMinute >= 60) {
//                     currentMinute -= 60;
//                     currentHour += 1;
//                 }
//             }

//             reservationTimeField.innerHTML = times.map(time => `<option value="${time}">${time}</option>`).join('');
//             console.log('Time options populated:', times);
//         }
//     }

//     // function clearTimeOptions() {
//     //     reservationTimeField.innerHTML = '<option value="">Select a time</option>';
//     // }

//     reservationDateField.addEventListener('change', changeReservationInput);
//     reservationLengthField.addEventListener('change', changeReservationInput);

//     // reservationForm.addEventListener('submit', function(event) {
//     //     const selectedTime = reservationTimeField.value;
//     //     if (selectedTime === '' || selectedTime === 'CLOSED') {
//     //         console.log("NO TIME DETECTED")
//     //         alert('Please select a valid reservation time.');
//     //         event.preventDefault(); // Prevent form submission if validation fails
//     //     }
//     // });
// });

document.addEventListener('DOMContentLoaded', function () {
    const reservationDateField = document.getElementById('id_reservation_date');
    const reservationLengthField = document.getElementById('id_reservation_length');
    const reservationTimeField = document.getElementById('id_reservation_time');
    const reservationForm = document.getElementById('reservation_form');

    let selectedTime = localStorage.getItem('selectedTime') || ''; // Retrieve selected time from localStorage

    function changeReservationInput() {
        const selectedDate = reservationDateField.value;
        const reservationLength = reservationLengthField.value;

        if (selectedDate) {
            fetchOpeningHours(selectedDate, reservationLength);
        } else {
            clearTimeOptions();
        }
    }

    function fetchOpeningHours(date, length) {
        console.log(`Fetching opening hours for date: ${date}`);
        fetch(`/booking/reservation/get_opening_hours/?date=${date}`)
            .then(response => response.json())
            .then(data => {
                console.log('Received data:', data);
                if (data.error) {
                    console.error(data.error);
                    clearTimeOptions();
                } else {
                    populateTimeOptions(data.opening_time, data.closing_time, length);
                }
            })
            .catch(error => {
                console.error('Error fetching opening hours:', error);
                clearTimeOptions();
            });
    }

    function populateTimeOptions(openingTime, closingTime, length) {
        if (openingTime === "00:00" && closingTime === "00:00") {
            console.log("CLOSED");
            reservationTimeField.innerHTML = null;
        } else {
            console.log(`Populating time options from ${openingTime} to ${length} hours before ${closingTime}`);
            const reservationLength = length;
            const [openingHour, openingMinute] = openingTime.split(':').map(Number);
            const [closingHour, closingMinute] = closingTime.split(':').map(Number);

            const times = [];
            let currentHour = openingHour;
            let currentMinute = openingMinute;

            while ((currentHour < closingHour) || (currentHour === closingHour && currentMinute <= closingMinute)) {
                var reservationEndHour = currentHour + Math.floor(reservationLength);
                var reservationEndMinute = currentMinute + (reservationLength % 1) * 60;
                if (reservationEndMinute >= 60) {
                    reservationEndHour += 1;
                    reservationEndMinute -= 60;
                }

                if (reservationEndHour < closingHour || (reservationEndHour === closingHour && reservationEndMinute <= closingMinute)) {
                    const formattedTime = `${String(currentHour).padStart(2, '0')}:${String(currentMinute).padStart(2, '0')}`;
                    times.push(formattedTime);
                }
                currentMinute += 15;
                if (currentMinute >= 60) {
                    currentMinute -= 60;
                    currentHour += 1;
                }
            }

            reservationTimeField.innerHTML = times.map(time => {
                return `<option value="${time}" ${time === selectedTime ? 'selected' : ''}>${time}</option>`;
            }).join('');
            scrollToAvailableTables();
            console.log('Time options populated:', times);
        }
    }

    function clearTimeOptions() {
        reservationTimeField.innerHTML = '<option value="">Select a time</option>';
    }

    function scrollToAvailableTables() {
        const availableTablesSection = document.getElementById('availableTables');
        if (availableTablesSection) {
            availableTablesSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Event listener for time field changes
    reservationTimeField.addEventListener('change', function() {
        selectedTime = reservationTimeField.value;
        localStorage.setItem('selectedTime', selectedTime); // Store selected time in localStorage
    });

    // Event listeners for input changes
    reservationDateField.addEventListener('change', changeReservationInput);
    reservationLengthField.addEventListener('change', changeReservationInput);

    // Trigger the function on page load if date and length are already selected
    if (reservationDateField.value && reservationLengthField.value) {
        changeReservationInput();
    }

    // Validate the form before submission
    reservationForm.addEventListener('submit', function (event) {
        const selectedTime = reservationTimeField.value;
        if (selectedTime === '' || selectedTime === 'CLOSED') {
            console.log("NO TIME DETECTED");
            alert('Please select a valid reservation time.');
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});
