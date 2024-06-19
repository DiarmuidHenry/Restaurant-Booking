console.log("Javascript file located and loaded")
document.addEventListener('DOMContentLoaded', function() {
    const reservationDateField = document.getElementById('id_reservation_date');
    const reservationTimeField = document.getElementById('id_reservation_time');

    reservationDateField.addEventListener('change', function() {
        const selectedDate = this.value;
        if (selectedDate) {
            fetchOpeningHours(selectedDate);
        } else {
            reservationTimeField.innerHTML = '<option value="">Error 1: Select a time</option>';
        }
    });

    function fetchOpeningHours(date) {
        console.log(`Fetching opening hours for date: ${date}`);
        fetch(`/get_opening_hours/?date=${date}`)
            .then(response => response.json())
            .then(data => {
                console.log('Received data:', data);
                if (data.error) {
                    console.error(data.error);
                    reservationTimeField.innerHTML = '<option value="">Error 2: Select a time</option>';
                } else {
                    populateTimeOptions(data.opening_time, data.closing_time);
                }
            })
            .catch(error => {
                console.error('Error fetching opening hours:', error);
                reservationTimeField.innerHTML = '<option value="">Error 3: Select a time</option>';
            });
    }

    function populateTimeOptions(openingTime, closingTime) {
        console.log(`Populating time options from ${openingTime} to ${closingTime}`);
        const reservationLength = 1; // Example reservation length in hours
        const [openingHour, openingMinute] = openingTime.split(':').map(Number);
        const [closingHour, closingMinute] = closingTime.split(':').map(Number);

        const times = [];
        let currentHour = openingHour;
        let currentMinute = openingMinute;

        while (currentHour < closingHour || (currentHour === closingHour && currentMinute < closingMinute - (reservationLength * 60))) {
            const formattedTime = `${String(currentHour).padStart(2, '0')}:${String(currentMinute).padStart(2, '0')}`;
            times.push(formattedTime);
            currentMinute += 15;
            if (currentMinute >= 60) {
                currentMinute -= 60;
                currentHour += 1;
            }
        }

        reservationTimeField.innerHTML = times.map(time => `<option value="${time}">${time}</option>`).join('');
        console.log('Time options populated:', times);
    }
});