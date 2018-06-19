const SpotifyWebApi = require('spotify-web-api-node');
const env = require('./env');

var spotify = new SpotifyWebApi(env.spotify.credentials);

// Create the authorization URL
var authorizeURL = spotify.createAuthorizeURL(env.spotify.scopes);
console.log(authorizeURL);
