const fs = require('fs');
const path = require('path');

// Función para escanear el directorio y calcular las estadísticas
function scanDir(dirPath, challenges = {}, languages = {}, total = 0, challengeName = null, pathName = null) {
    const files = fs.readdirSync(dirPath, { withFileTypes: true });

    files.forEach(file => {
        const fullPath = path.join(dirPath, file.name);

        if (file.isDirectory()) {
            if (file.name.includes("Reto #") && !challenges[file.name]) {
                challenges[file.name] = 0;
                challengeName = file.name;
            } else if (!file.name.includes("Reto #") && !languages[file.name]) {
                languages[file.name] = 0;
            }

            // Recursivamente escanear subdirectorios
            [challenges, languages, total] = scanDir(fullPath, challenges, languages, total, challengeName, file.name);
        } else {
            if (pathName in languages) {
                total += 1;
                if (challengeName) challenges[challengeName] += 1;
                languages[pathName] += 1;
            }
        }
    });

    return [challenges, languages, total];
}

// Directorio de retos a analizar, ajustado a la carpeta `listado` en la raíz del proyecto
const dirPath = path.join(__dirname, 'listado');

// Escanear el directorio y obtener estadísticas
let [challenges, languages, total] = scanDir(dirPath);

// Ordenar retos y lenguajes por uso (de mayor a menor)
challenges = Object.fromEntries(
    Object.entries(challenges).sort(([, a], [, b]) => b - a)
);

languages = Object.fromEntries(
    Object.entries(languages).sort(([, a], [, b]) => b - a)
);

// Construir el contenido del README
let readmeContent = `# Estadísticas de los Retos de Programación\n\n`;
readmeContent += `> ${Object.keys(languages).length} LENGUAJES (${total} CORRECCIONES)\n\n`;

Object.keys(challenges).forEach(challenge => {
    const percentage = ((challenges[challenge] / total) * 100).toFixed(2);
    readmeContent += `> ${challenge.toUpperCase()} (${challenges[challenge]}): ${percentage}%\n`;
});

readmeContent += `\n`;

Object.keys(languages).forEach(language => {
    const percentage = ((languages[language] / total) * 100).toFixed(2);
    readmeContent += `> ${language.toUpperCase()} (${languages[language]}): ${percentage}%\n`;
});

// Escribir el contenido al archivo README.md
const readmePath = path.join(__dirname, 'README.md');
fs.writeFileSync(readmePath, readmeContent, 'utf8');

console.log('Estadísticas generadas y guardadas en README.md');
