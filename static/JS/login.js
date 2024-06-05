document.addEventListener('DOMContentLoaded', (event) => {
    const modal = document.getElementById('modal');
    const openModalBtn = document.getElementById('openModalBtn');
    const closeBtn = document.getElementsByClassName('close-btn')[0];

    openModalBtn.onclick = function() {
        modal.style.display = 'flex';
    }

    closeBtn.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});