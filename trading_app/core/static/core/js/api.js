


document.addEventListener('DOMContentLoaded', function() {
    // Code to run when page is loaded
    console.log("Page loaded");
});


function getFormData(formId) {
    const form = document.getElementById(formId);
    const formData = new FormData(form);
    // Convert FormData to a plain object
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });
    return data;
}

// Example usage: call another function with the form data
document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const data = getFormData('myForm');
    useFormData(data); // Pass data to another function
});

function useFormData(data) {
    // You can use the form data here
    console.log(data);
}

