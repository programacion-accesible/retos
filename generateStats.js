const fs = require('fs');
const path = require('path');

// Directorio de retos a analizar
const dirPath = path.join(__dirname, 'listado');
const outputPath = path.join(__dirname, 'cliente', 'stats.json'); // Archivo donde guardaremos las estadísticas

// Función para escanear el directorio y calcular las estadísticas
function scanDir(dirPath, challenges = {}, languages = {}, participants = {}, total = 0, challengeName = null, pathName = null) {
    const files = fs.readdirSync(dirPath, { withFileTypes: true });

    files.forEach(file => {
        const fullPath = path.join(dirPath, file.name);

        if (file.isDirectory()) {
            // Si es un directorio que contiene un reto
            if (file.name.includes("Reto #") && !challenges[file.name]) {
                challenges[file.name] = 0;
                challengeName = file.name;
            } else if (!file.name.includes("Reto #") && !languages[file.name]) {
                languages[file.name] = 0;
            }

            // Recursivamente escanear subdirectorios
            [challenges, languages, participants, total] = scanDir(fullPath, challenges, languages, participants, total, challengeName, file.name);
        } else {
            // Contar archivos en lenguajes
            if (pathName in languages) {
                total += 1;
                if (challengeName) challenges[challengeName] += 1;
                languages[pathName] += 1;

                // Contar participantes
                const participantName = path.basename(fullPath, path.extname(fullPath)); // Obtener el nombre del participante sin la extensión
                participants[participantName] = (participants[participantName] || 0) + 1;
            }
        }
    });

    return [challenges, languages, participants, total];
}

// Función para calcular el porcentaje
function calculatePercentage(count, total) {
    return total > 0 ? ((count / total) * 100).toFixed(2) : 0;
}

// Emitir estadísticas y guardarlas en archivo JSON
function emitStats() {
    // Escanear el directorio y obtener estadísticas
    let [challenges, languages, participants, total] = scanDir(dirPath);

    // Ordenar retos y lenguajes por uso (de mayor a menor)
    challenges = Object.fromEntries(
        Object.entries(challenges).sort(([, a], [, b]) => b - a)
    );

    languages = Object.fromEntries(
        Object.entries(languages).sort(([, a], [, b]) => b - a)
    );

    // Preparar datos para enviar
    const sortedChallenges = Object.keys(challenges).map(challenge => ({
        name: challenge,
        count: challenges[challenge],
        percentage: calculatePercentage(challenges[challenge], total)
    }));

    const sortedLanguages = Object.keys(languages).map(language => ({
        name: language,
        count: languages[language],
        percentage: calculatePercentage(languages[language], total)
    }));

    const sortedParticipants = Object.keys(participants).map(participant => ({
        name: participant,
        count: participants[participant],
        percentage: calculatePercentage(participants[participant], total)
    }));

    const stats = {
        challenges: sortedChallenges,
        languages: sortedLanguages,
        participants: sortedParticipants,
        total: total,
        languageCount: Object.keys(languages).length,
        lastUpdated: new Date().toISOString()
    };

    // Guardar en un archivo JSON
    fs.writeFileSync(outputPath, JSON.stringify(stats, null, 2));
    console.log('Estadísticas generadas y guardadas en stats.json');
}

// Llamar a la función para emitir estadísticas
emitStats();
