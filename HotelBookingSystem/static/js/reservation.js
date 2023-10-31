// Get references to the input fields and the element to display the total price
const roomInput = document.getElementById("room-id");
const checkInInput = document.getElementById("check-in");
const checkOutInput = document.getElementById("check-out");
const duration = document.getElementById("duration");
const totalPriceDisplay = document.getElementById("total-price");

// Event listener for any changes in the input fields
roomInput.addEventListener("input", updateTotalPrice);
checkInInput.addEventListener("input", updateTotalPrice);
checkOutInput.addEventListener("input", updateTotalPrice);

// Function to calculate and update the total booking amount
function updateTotalPrice() {
    const roomID = roomInput.value;
    const checkIn = checkInInput.valueAsDate;
    const checkOut = checkOutInput.valueAsDate;

    if (roomID && checkIn && checkOut) {
        // Send an AJAX request to the Django view to get room pricing
        fetch("/get-room-pricing/${roomID}")
            .then(response => response.json())
            .then(data => {
                if (data.available) {
                    document.getElementById("available-results").innerHTML = `
                    <p>Room is available for ${data.duration} nights.</p>
                    <p>Total Price: $${data.total_price}</p>
                    <button id="book-button">Book Now</button>
                `;
                    
                } else {
                   document.getElementById("available-results").innerHTML = "Room not available for the selected dates";
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
    } 
}
