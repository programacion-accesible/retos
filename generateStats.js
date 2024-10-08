const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fs = require('fs');
const path = require('path');

const app = express();
const server = http.createServer(app);

// Habilitar CORS en Socket.io
const io = socketIo(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

// Directorio de retos a analizar
const dirPath = path.join(__dirname, 'listado');

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

// Emisión de las estadísticas a través de Socket.io
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

    io.emit('updateStats', {
        challenges: sortedChallenges,
        languages: sortedLanguages,
        participants: sortedParticipants,
        total: total,
        languageCount: Object.keys(languages).length,
        lastUpdated: new Date().toISOString()
    });
}

// Emitir estadísticas cada vez que un cliente se conecta
io.on('connection', (socket) => {
    console.log('Cliente conectado');
    emitStats();

    socket.on('disconnect', () => {
        console.log('Cliente desconectado');
    });
});

// Iniciar el servidor
server.listen(3000, () => {
    console.log('Servidor escuchando en puerto 3000');
});
