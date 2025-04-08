/**
 * generateRandomDataset.js
 * 
 * Este script utiliza la función generateDataset(numCentroids, nPointsPerCluster)
 * 
 * Para generar un conjunto de datos sintéticos distribuidos en varios clústeres.
 * 
 * Para usarlo en la terminarl:
 *             node generateRandomDataset.js 3 100
 * 
 * Cuando lo usemos en el navegador, retornara un objeto con los puntos y sus centros.
 *          puntos: {x, y, originalCluster, predictedCluster}
 *          centros: {x, y, desviación}
 */

function generateDataset(numCentroids, nPointsPerCluster){
    
    const points = []; // Almacena los puntos
    const centers = []; // Almacena los centros

    const margin = 50;
    const canvasSize = 700;

    // 1) Generar las coordenadas aleatorias para cada centro
    for (let i = 0; i < numCentroids ; i++) {
        const randX = Math.random() * (canvasSize - margin);
        const randY = Math.random() * (canvasSize - margin);
        const randDesv = Math.random() * 100;
        centers.push({x: randX, y: randY, desv: randDesv})
    }

    // 2) Generamos los puntos pertenecientes a cada centro
    centers.forEach((center, clusterIndex) => {
        for(let i = 0; i < nPointsPerCluster; i++){
            let x = center.x + (Math.random() - 0.5) * center.desv;
            let y = center.y + (Math.random() - 0.5) * center.desv;

            // Registramos el punto dentro de los puntos asociados al cluster
            points.push({x, y, originalClusters:clusterIndex, predictedCluster: null})
        }
    })

    return {points, centers};
}

/**
 * convertToCSV: convierte un array de objetos JS a CSV
 */

function convertToCSV(data){
    // Generamos la cabecera de nuestro CSV: utilizaremos las claves del primer objeto
    const header = Object.keys(data[0]).join(",");
    const rows = data.map(row => Object.values(row).join(","));
    return [header, ...rows].join("\n");
}

/**
 * Antes de continuar, vamos a comprobar si existe un objeto llamado "module" qué solo se utiliza en Node.js
 * 
 * Este objeto tiene un método .exports que es un mecanismo para exportar funciones.
 */

if (typeof module !== "undefined" && module.exports) {
    module.exports = { generateDataset };
 
    if (require.main === module) {
      const fs = require('fs');
      const path = require('path');
 
      // 1) Tomamos argumentos de la CLI: numCentroids y nPointsPerCluster
      const args = process.argv.slice(2);
      const numCentroids = parseInt(args[0]) || 3;       // Valor por defecto: 3 clusters
      const nPointsPerCluster = parseInt(args[1]) || 50; // Valor por defecto: 50 puntos/cluster
 
      // 2) Llamamos a generateDataset para obtener los puntos
      const { points } = generateDataset(numCentroids, nPointsPerCluster);
 
      // 3) Transformamos a CSV
      const csvContent = convertToCSV(points);
 
      // 4) Escribimos en un archivo local “data.csv”
      const outputFileName = "data.csv";
      const filePath = path.join(__dirname, outputFileName);
 
      fs.writeFile(filePath, csvContent, (err) => {
        if (err) {
          console.error("Error al guardar el archivo CSV:", err);
        } else {
          console.log(`Archivo CSV "${outputFileName}" creado con ${points.length} puntos.`);
        }
      });
    }
  } else {
    // Si no estamos en Node (CLI), se asume que estamos en un navegador.
    // Exponemos la función en la variable window para que otros scripts puedan usarla.
    window.generateDataset = generateDataset;
  }