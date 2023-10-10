// navbar
function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
  }

//   modal for slot appointment

// document.addEventListener("DOMContentLoaded", function () {
//     const openAppointmentModalButtons = document.querySelectorAll(".openModalButton");
//     const appointmentModal = document.getElementById("modal-section");
//     const closeModalButton = document.querySelector(".modal-cancel");
//     const doctorNameTitle = document.getElementById("doctorNameTitle");
//     const dentalServiceTitle = document.getElementById("dentalServiceTitle");
//     const slotDateInput = document.getElementById("slotDateInput");
//     const slotTimeInput = document.getElementById("slotTimeInput");
//     const slotUserEmail = document.getElementById("slotUserEmail");

//     openAppointmentModalButtons.forEach(function (button) {
//         button.addEventListener("click", function () {
//             const doctorName = button.getAttribute("data-doctor-name");
//             const dentalServiceName = button.getAttribute("data-dental-service");
//             const slotDate = button.getAttribute("data-slot-date");
//             const slotStartTime = button.getAttribute("data-slot-start-time");
//             const slotEndTime = button.getAttribute("data-slot-end-time");
//             const slotEmail = button.getAttribute("data-slot-email");
//             const slotId = button.getAttribute("data-slot-id");

          
//             doctorNameTitle.textContent = doctorName;
//             dentalServiceTitle.textContent = dentalServiceName;
//             slotDateInput.value = slotDate; // Set the value of date input
//             slotTimeInput.value = slotStartTime + " - " + slotEndTime; // Set the value of time input
//             slotUserEmail.value = slotEmail;
//             appointmentModal.style.display = "block";
//         });
//     });

//     closeModalButton.addEventListener("click", function () {
//         appointmentModal.style.display = "none";
//     });

   
//     window.addEventListener("click", function (event) {
//         if (event.target === appointmentModal) {
//             appointmentModal.style.display = "none";
//         }
//     });
// });


document.addEventListener("DOMContentLoaded", function () {
    const openAppointmentModalButtons = document.querySelectorAll(".openModalButton");
    const appointmentModal = document.getElementById("modal-section");
    const closeModalButton = document.querySelector(".modal-cancel");
    const doctorNameTitle = document.getElementById("doctorNameTitle");
    const dentalServiceTitle = document.getElementById("dentalServiceTitle");
    const slotDateInput = document.getElementById("slotDateInput");
    const slotTimeInput = document.getElementById("slotTimeInput");
    const slotUserEmail = document.getElementById("slotUserEmail");

    openAppointmentModalButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const doctorName = button.getAttribute("data-doctor-name");
            const dentalServiceName = button.getAttribute("data-dental-service");
            const slotDate = button.getAttribute("data-slot-date");
            const slotStartTime = button.getAttribute("data-slot-start-time");
            const slotEndTime = button.getAttribute("data-slot-end-time");
            const slotEmail = button.getAttribute("data-slot-email");
            const slotId = button.getAttribute("data-slot-id");

            doctorNameTitle.textContent = doctorName;
            dentalServiceTitle.textContent = dentalServiceName;
            slotDateInput.value = slotDate;
            slotTimeInput.value = slotStartTime + " - " + slotEndTime;
            slotUserEmail.value = slotEmail;
        
            const slotIdInput = document.createElement("input");
            slotIdInput.type = "hidden";
            slotIdInput.name = "slotId";  // Use the same name as expected in your view
            slotIdInput.value = slotId;
            appointmentForm.appendChild(slotIdInput);

            appointmentModal.style.display = "block";
        });
    });

    closeModalButton.addEventListener("click", function () {
        appointmentModal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === appointmentModal) {
            appointmentModal.style.display = "none";
        }
    });

    const appointmentForm = document.getElementById("appointmentForm");
    appointmentForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData(appointmentForm);
//         const currentUrl = window.location.href;
// const endpoint = "/bookAppointment/";
// const apiUrl = currentUrl.replace(/\/slots\/\d+\//, endpoint);

// fetch(apiUrl, {
//     method: "POST",
//     body: formData,
// })

        const currentUrl = window.location.href;
        console.log(currentUrl)
const endpoint = "/bookAppointment/";
const apiUrl = currentUrl.replace(/\/slots\/\d+\//, endpoint);
console.log(apiUrl)
        fetch(apiUrl, {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {    
            // console.log(data)
            // console.log(data.message);
            appointmentModal.style.display = "none";
            if (data.success){
                // console.log('success')
                window.location.href = data.dashboard_url;
            }
            
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});







 




