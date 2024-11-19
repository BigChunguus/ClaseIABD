db = connect('mongosh "mongodb+srv://basesdatosaplicado.bq8ju.mongodb.net/" --apiVersion 1 --username iabd12')
for (let i = 0; i < 100; i++) {
    db.estudiantes.insertOne({
        nombre: "Alumno" + i,
        edad: 20 + i,
        curso: "iabd"
    });
}

print("100 estudiantes insertados correctamente.");
