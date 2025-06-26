// Example: Add a simple alert on form submit
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function() {
            alert('Image submitted for prediction!');
        });
    }
});