// login.js
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Evita el refresco de la página
        
        const username = document.getElementById('username').value;
        
        // Guardamos el nombre de usuario en localStorage
        localStorage.setItem('chatUsername', username);

        // Redirigimos a la pantalla del chat
        window.location.href = 'chat.html';
    });
});
