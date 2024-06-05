document.addEventListener('DOMContentLoaded', function() {
    const errorMessages = document.querySelectorAll('.alert');
    let combinedErrors = '';

    errorMessages.forEach((error) => {
        const errorText = error.textContent.trim();
        if (errorText !== '') {
            combinedErrors += errorText + '\n';  // Собираем все ошибки в одну строку
        }
    });

    if (combinedErrors !== '') {
        showAlert(combinedErrors.trim());
    }
});

function showAlert(message) {
    const alertBox = document.createElement('div');
    alertBox.classList.add('alert', 'show');
    alertBox.textContent = message;
    document.body.appendChild(alertBox);

    // Убедимся, что уведомление остается видимым в течение 3 секунд
    setTimeout(() => {
        alertBox.classList.remove('show');
        alertBox.style.display = 'none';
    }, 5000);
}