import tkinter as tk

# Configuración de la ventana principal
window = tk.Tk()
window.title("Chatbot con Widgets Simulados")
window.geometry("525x425")

# Crear un canvas para dibujar el degradado de fondo de la ventana
canvas = tk.Canvas(window, width=525, height=425)
canvas.pack(fill="both", expand=True)

# Función para crear un degradado en un canvas específico
def create_diagonal_gradient(canvas, start_color, end_color, width, height):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    steps = max(width, height)
    
    for i in range(steps):
        r = int(r1 + (r2 - r1) * (i / steps))
        g = int(g1 + (g2 - g1) * (i / steps))
        b = int(b1 + (b2 - b1) * (i / steps))
        color = f'#{r:02x}{g:02x}{b:02x}'
        
        x0, y0 = i, 0
        x1, y1 = 0, i
        canvas.create_rectangle(x0, y0, width, height, outline=color, fill=color)

# Crear degradado de fondo de la ventana
create_diagonal_gradient(canvas, (234, 151, 255), (200, 200, 255), 525, 425)

# Crear un área simulada de chat con degradado
chat_canvas = tk.Canvas(canvas, width=440, height=220, highlightthickness=0)
create_diagonal_gradient(chat_canvas, (255, 223, 186), (186, 255, 201), 440, 220)
chat_canvas.place(x=42, y=30)

# Simular mensaje en el área de chat
chat_canvas.create_text(220, 110, text="Bienvenido al chatbot con degradado!", font=("Arial", 12), fill="#333333")

# Crear un botón simulado con degradado
button_canvas = tk.Canvas(canvas, width=80, height=30, highlightthickness=0)
create_diagonal_gradient(button_canvas, (135, 206, 235), (72, 61, 139), 80, 30)
button_canvas.place(x=220, y=370)
button_canvas.create_text(40, 15, text="Enviar", font=("Arial", 10, "bold"), fill="#ffffff")

# Caja de entrada de texto simulada (sin función de entrada)
entry_canvas = tk.Canvas(canvas, width=440, height=30, highlightthickness=0, bg="#dfe7ee")
entry_canvas.place(x=42, y=310)
entry_canvas.create_text(10, 15, anchor="w", text="Escribe aquí tu mensaje...", font=("Arial", 10), fill="#333333")

# Iniciar la interfaz
window.mainloop()
