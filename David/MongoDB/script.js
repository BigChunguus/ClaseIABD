// a) Cantidad de documentos correspondientes a la ciudad de SAN DIEGO
db.zips.countDocuments({ city: "SAN DIEGO" });

// b) Documentos con menos de 100 habitantes (campo pop)
db.zips.countDocuments({ pop: { $lt: 100 } });

// c) Estados asociados a la ciudad SAN DIEGO
db.zips.distinct("state", { city: "SAN DIEGO" });

// d) Código postal de la ciudad ALLEN que no tiene habitantes (devuelve solo el campo zip)
db.zips.find({ city: "ALLEN", pop: 0 }, { zip: 1, _id: 0 });

// e) Los 5 códigos postales más poblados (incluye todos los campos de los documentos)
db.zips.find().sort({ pop: -1 }).limit(5);

// f) Documentos que no tienen menos de 5,000 habitantes ni más de 1,000,000 (usando $nor)
db.zips.countDocuments({ $nor: [{ pop: { $lt: 5000 } }, { pop: { $gt: 1000000 } }] });

// g) Documentos con más habitantes que el valor de su propio código postal (campo zip)
db.zips.countDocuments({ $expr: { $gt: ["$pop", { $toInt: "$zip" }] } });

// a) Cuenta cuántos mensajes contienen las etiquetas restaurant o moon
db.posts.countDocuments({ tags: { $in: ["restaurant", "moon"] } });

// b) Recupera los comentarios escritos por el usuario Salena Olmos
db.posts.find({ "comments.author": "Salena Olmos" }, { "comments.$": 1, _id: 0 });

// c) Encuentra los mensajes cuyo cuerpo (body) contenga la palabra earth
// Devuelve: el título, tres comentarios y cinco etiquetas
db.posts.find(
  { body: { $regex: "earth", $options: "i" } },
  { title: 1, comments: { $slice: 3 }, tags: { $slice: 5 }, _id: 0 }
);


// ** 3.1 Inserciones **

// a) Crear un documento con los datos proporcionados
db.zips.insertOne({
    city: "ELX",
    zip: "03206",
    loc: { x: 38.265500, y: -0.698459 },
    pop: 230224,
    state: "España"
});

// b) Crear un documento con el código postal de tu lugar de residencia (ejemplo con un código ficticio)
db.zips.insertOne({
    city: "TU_CIUDAD",
    zip: "12345",
    loc: { x: 40.1234, y: -3.4567 },
    pop: 10000,
    state: "España"
});

// ** 3.2 Actualizaciones **

// a) Cambiar la población de tu código postal a 1,000,000
db.zips.updateOne({ zip: "12345" }, { $set: { pop: 1000000 } });

// b) Incrementar la población de todos los documentos con state: "España" en 666 personas
db.zips.updateMany({ state: "España" }, { $inc: { pop: 666 } });

// c) Añadir un nuevo campo prov con el valor "Alicante" a ambos documentos
db.zips.updateMany({ state: "España" }, { $set: { prov: "Alicante" } });

// d) Añadir un atributo tags con un array vacío a todos los documentos donde state: "España"
db.zips.updateMany({ state: "España" }, { $set: { tags: [] } });

// e) Actualizar todos los documentos de la provincia de Alicante para añadir el valor sun al atributo tags
db.zips.updateMany({ prov: "Alicante" }, { $push: { tags: "sun" } });

// f) Sustituir el valor sun por house en el atributo tags de tu documento
db.zips.updateOne(
    { zip: "12345" },
    { $set: { "tags.$[elemento]": "house" } },
    { arrayFilters: [{ elemento: "sun" }] }
);

// g) Renombrar el campo prov como provincia en todos los documentos de la provincia de Cantabria
db.zips.updateMany({ prov: "Cantabria" }, { $rename: { prov: "provincia" } });

// ** 3.3 Eliminaciones **

// a) Eliminar el atributo loc del documento con zip: "39700"
db.zips.updateOne({ zip: "39700" }, { $unset: { loc: "" } });

// b) Eliminar el documento que contiene el código postal que creaste en tu lugar de residencia
db.zips.deleteOne({ zip: "12345" });
