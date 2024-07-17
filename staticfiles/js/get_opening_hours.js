document.addEventListener('DOMContentLoaded', function () {
    const reservationDateField = document.getElementById('id_reservation_date');
    const reservationLengthField = document.getElementById('id_reservation_length');
    const reservationTimeField = document.getElementById('id_reservation_time');

    let selectedTime = localStorage.getItem('selectedTime') || ''; // Retrieve selected time from localStorage

    function changeReservationInput() {
        const selectedDate = reservationDateField.value;
        const reservationLength = parseFloat(reservationLengthField.textContent);

        if (selectedDate) {
            fetchOpeningHours(selectedDate, reservationLength);
        } else {
            clearTimeOptions();
        }
    }

    function fetchOpeningHours(date, length) {
        fetch(`/booking/reservation/get_opening_hours/?date=${date}`)
            .then(response => response.json())
            .then(data => {
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
            reservationTimeField.innerHTML = null;
        } else {
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
            scrollToAlertMessage();
        }
    }

    function clearTimeOptions() {
        reservationTimeField.innerHTML = '<option value="">Select a time</option>';
    }

    function scrollToAvailableTables() {
        const availableTablesSection = document.getElementById('availableTables');
        if (availableTablesSection) {
            availableTablesSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    function scrollToAlertMessage() {
        const alertMessageSection = document.getElementById('alertMessage');
        if (alertMessageSection) {
            alertMessageSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    // Event listener for time field changes
    reservationTimeField.addEventListener('change', function () {
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

});
