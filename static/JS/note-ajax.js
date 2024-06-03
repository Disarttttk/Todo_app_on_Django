//const toDoInput = document.querySelector('.todo-input');
//const toDoBtn = document.querySelector('.todo-btn');
//const toDoList = document.querySelector('.todo-list');
//const standardTheme = document.querySelector('.standard-theme');
//const lightTheme = document.querySelector('.light-theme');
//const darkerTheme = document.querySelector('.darker-theme');
//
//
//standardTheme.addEventListener('click', () => changeTheme('standard'));
//lightTheme.addEventListener('click', () => changeTheme('light'));
//darkerTheme.addEventListener('click', () => changeTheme('darker'));

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
  var checkButtons = document.querySelectorAll('.check-btn');
  checkButtons.forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        var itemId = this.getAttribute('data-id');
        var url = this.getAttribute('data-note-check-url')
        var parentElement = this.parentElement;

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
              parentElement.classList.toggle('completed');
//            if(data.status){
//                parentElement.classList.add('completed');
//            } else {
//                parentElement.classList.remove('completed');
//            }

          } else {
            // Обработка ошибки, если сервер вернул ошибку
            alert('Ошибка при изменении статуса: ' + data.error);
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

//// Change theme function:
//function changeTheme(color) {
//    localStorage.setItem('savedTheme', color);
//    savedTheme = localStorage.getItem('savedTheme');
//
//    document.body.className = color;
//    // Change blinking cursor for darker theme:
//    color === 'darker' ?
//        document.getElementById('title').classList.add('darker-title')
//        : document.getElementById('title').classList.remove('darker-title');
//
//    document.querySelector('input').className = `${color}-input`;
//    // Change todo color without changing their status (completed or not):
//    document.querySelectorAll('.todo').forEach(todo => {
//        Array.from(todo.classList).some(item => item === 'completed') ?
//            todo.className = `todo ${color}-todo completed`
//            : todo.className = `todo ${color}-todo`;
//    });
//    // Change buttons color according to their type (todo, check or delete):
//    document.querySelectorAll('button').forEach(button => {
//        Array.from(button.classList).some(item => {
//            if (item === 'check-btn') {
//              button.className = `check-btn ${color}-button`;
//            } else if (item === 'delete-btn') {
//                button.className = `delete-btn ${color}-button`;
//            } else if (item === 'todo-btn') {
//                button.className = `todo-btn ${color}-button`;
//            }
//        });
//    });
//}
