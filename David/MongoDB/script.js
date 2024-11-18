// a
db.zips.countDocuments({ city: "SAN DIEGO" });

// b
db.zips.countDocuments({ pop: { $lt: 100 } });

// c
db.zips.distinct("state", { city: "SAN DIEGO" });

// d
db.zips.find({ city: "ALLEN", pop: 0 }, { zip: 1, _id: 0 });

// e
db.zips.find().sort({ pop: -1 }).limit(5);

// f
db.zips.countDocuments({ $nor: [{ pop: { $lt: 5000 } }, { pop: { $gt: 1000000 } }] });

// g
db.zips.countDocuments({ $expr: { $gt: ["$pop", { $toInt: "$zip" }] } });

// a
db.posts.countDocuments({ tags: { $in: ["restaurant", "moon"] } });

// b
db.posts.find({ "comments.author": "Salena Olmos" }, { "comments.$": 1, _id: 0 });

// c
db.posts.find(
  { body: { $regex: "earth", $options: "i" } },
  { title: 1, comments: { $slice: 3 }, tags: { $slice: 5 }, _id: 0 }
);

// 3.1 a
db.zips.insertOne({
  city: "ELX",
  zip: "03206",
  loc: { x: 38.265500, y: -0.698459 },
  pop: 230224,
  state: "España"
});

// 3.1 b
db.zips.insertOne({
  city: "Castro Urdiales",
  zip: "39700",
  loc: { x: 40.1234, y: -3.4567 },
  pop: 200000,
  state: "España"
});

// 3.2 a
db.zips.updateOne({ zip: "39700" }, { $set: { pop: 1000000 } });

// 3.2 b
db.zips.updateMany({ state: "España" }, { $inc: { pop: 666 } });

// 3.2 c
db.zips.updateMany({ state: "España" }, { $set: { prov: "Alicante" } });

// 3.2 d
db.zips.updateMany({ state: "España" }, { $set: { tags: [] } });

// 3.2 e
db.zips.updateMany({ prov: "Alicante" }, { $push: { tags: "sun" } });

// 3.2 f
db.zips.updateOne(
  { zip: "39700" },
  { $set: { "tags.$[elemento]": "house" } },
  { arrayFilters: [{ elemento: "sun" }] }
);

// 3.2 g
db.zips.updateMany({}, { $rename: { prov: "Cantabria" } });

// 3.3 a
db.zips.updateOne({ zip: "39700" }, { $unset: { loc: "" } });

// 3.3 b
db.zips.deleteOne({ zip: "39700" });
