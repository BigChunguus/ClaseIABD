db = connect('mongodb+srv://iabd12:iabdiabd12@basesdatosaplicado.bq8ju.mongodb.net/Escuela');

const estudiantes = db.estudiantes;

for (let i = 11000; i < 1000000; i++) {
    estudiantes.insertOne({
        nombre: "Alumno" + i,
        edad: 20 + i,
        curso: "iabd"
    });
    print(i);
}

print("100000 estudiantes insertados correctamente.");
