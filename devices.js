const env = require('./env');
const SpotifyWebApi = require('spotify-web-api-node');
var spotifyAPI = new SpotifyWebApi(env.spotify.credentials);

spotifyAPI
    .refreshAccessToken()
    .then(function (data) {
        console.log(JSON.stringify(data.body));
        spotifyAPI.setAccessToken(data.body['access_token']);

        return spotifyAPI.getMyDevices();
    }).then(function (data) {
        console.log(JSON.stringify(data.body));
    }).catch(function (err) {
        console.log(JSON.stringify(err));
    });