

console.log('code execute')

// Get the success modal and close button elements
const successModal = document.getElementById('successModal');
const closeBtn = document.getElementById('closeBtn');

// Function to show the success modal
function showSuccessModal() {
    successModal.style.display = 'block';
    console.log('code execute')

    // Automatically close the success modal after 5 seconds
    setTimeout(function () {
        successModal.style.display = 'none';
    }, 5000);
}

// Event listener for closing the success modal
closeBtn.addEventListener('click', function () {
    console.log('click')
    successModal.style.display = 'none';
});

// Show the success modal
showSuccessModal();
