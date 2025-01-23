const RPC = require('discord-rpc');

// ID de l'application Discord (crée une application sur https://discord.com/developers/applications)
const clientId = '1332074949648846910';

// Crée un client RPC
const rpc = new RPC.Client({ transport: 'ipc' });

rpc.on('ready', () => {
    console.log('Rich Presence connecté à Discord.');

    // Définit l'activité de Rich Presence
    rpc.setActivity({
        details: 'Écoute RadioRapGo 🎧',
        state: 'En streaming musical',
        startTimestamp: Date.now(),
        largeImageKey: 'circle-shape-with-podcast-microphone-and-wifi-symbol-free-vector', // Ajoute une image dans l'onglet "Rich Presence > Art Assets"
        largeImageText: 'RadioRapGo',
        buttons: [
      { label: 'Écouter en direct', url: 'https://azulfrance.vercel.app/radiorapgo' }
        ],
    });
});

rpc.login({ clientId }).catch(console.error);
