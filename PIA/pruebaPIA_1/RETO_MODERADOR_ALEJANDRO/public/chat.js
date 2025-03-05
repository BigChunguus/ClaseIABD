// chat.js
document.addEventListener('DOMContentLoaded', () => {
    // 1. Recuperamos el usuario
    const currentUser = localStorage.getItem('chatUsername');
    const currentUserSpan = document.getElementById('currentUser');
    currentUserSpan.textContent = currentUser;

    // Elementos del DOM
    const chatMessagesDiv = document.getElementById('chatMessages');
    const messageInput = document.getElementById('messageInput');
    const sendBtn = document.getElementById('sendBtn');

    // 2. Función para cargar los últimos 10 mensajes
    async function loadMessages() {
        try {
            const response = await fetch('/api/messages'); 
            // La ruta '/messages' la crearemos en el servidor Node.js
            const messages = await response.json();

            // Limpiar el contenedor de mensajes
            chatMessagesDiv.innerHTML = '';

            // Insertar cada mensaje en el contenedor
            messages.forEach(msg => {
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('message');

                const userSpan = document.createElement('span');
                userSpan.classList.add('message-user');
                userSpan.textContent = `${msg.usuario}: `;

                const textSpan = document.createElement('span');
                textSpan.textContent = msg.texto;

                const timeSpan = document.createElement('div');
                timeSpan.classList.add('message-time');
                timeSpan.textContent = msg.hora;

                messageDiv.appendChild(userSpan);
                messageDiv.appendChild(textSpan);
                messageDiv.appendChild(timeSpan);

                chatMessagesDiv.appendChild(messageDiv);
            });
        } catch (error) {
            console.error('Error al cargar mensajes:', error);
        }
    }

    // 3. Función para enviar un nuevo mensaje
    async function sendMessage() {
        const messageText = messageInput.value.trim();
        if (!messageText) return;

        const data = {
            usuario: currentUser,
            texto: messageText
        };

        try {
            await fetch('/api/messages', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            messageInput.value = '';
            // Recargamos los mensajes para que se vea el que acabamos de enviar
            loadMessages();
        } catch (error) {
            console.error('Error al enviar mensaje:', error);
        }
    }

    // Evento del botón de enviar
    sendBtn.addEventListener('click', sendMessage);

    // Permitir enviar con Enter
    messageInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    // 4. Cargamos inicialmente los mensajes
    loadMessages();

    // 5. Actualizamos los mensajes cada 5 segundos (opcional)
    setInterval(loadMessages, 5000);
});
