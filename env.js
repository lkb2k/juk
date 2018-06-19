require('dotenv').config();
module.exports = {
    spotify: {
        credentials: {
            clientId: process.env.SPOTIFY_CLIENT_ID,
            clientSecret: process.env.SPOTIFY_CLIENT_SECRET,
            redirectUri: 'http://localhost/callback',
            refreshToken:process.env.SPOTIFY_REFRESH_CODE,
        },
        scopes: ['user-read-private', 'streaming', 'user-modify-playback-state', 'user-read-playback-state', 'user-read-currently-playing', 'playlist-read-private']
    }
};

