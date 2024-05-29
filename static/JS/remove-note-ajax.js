document.addEventListener('DOMContentLoaded', function() {
  // Получаем все кнопки с классом 'delete-btn' и добавляем им обработчики события
  var deleteButtons = document.querySelectorAll('.delete-btn');
  deleteButtons.forEach(function(button) {
    button.addEventListener('click', function(e) {
      e.preventDefault();
      var itemId = this.getAttribute('data-id'); // Извлекаем ID элемента
      var url = this.getAttribute('data-note-delete-url')
      var parentElement = this.parentElement; // Получаем родительский элемент кнопки
      function removeElementAfterAnimation() {
        parentElement.remove(); // Удаление элемента из DOM после анимации
      }
      // Отправляем AJAX запрос на сервер
      fetch(url, { // Измените URL на URL вашего обработчика удаления
        method: 'POST',
        body: JSON.stringify({id: itemId}),
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCSRFToken() // Функция getCSRFToken должна возвращать текущий CSRF токен
        }
      }).then(response => response.json())
        .then(data => {
          if(data.success) {
          // Добавляем класс анимации перед началом удаления элемента
            parentElement.classList.add('fall');
            // Если сервер подтвердил удаление, удаляем элемент из DOM
            parentElement.addEventListener('animationend', removeElementAfterAnimation, {once: true});
          } else {
            // Обработка ошибки, если сервер вернул ошибку
            alert('Ошибка при удалении: ' + data.error);
          }
        }).catch(error => {
          console.error('Ошибка AJAX запроса:', error);
        });
    });
  });
});


function getCSRFToken() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}