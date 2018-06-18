var SpotifyWebApi = require('spotify-web-api-node');

// credentials are optional
var spotifyApi = new SpotifyWebApi({
  clientId: 'f4e5e94a0eb84444af47c70ee85a8434',
  redirectUri: 'http://localhost/callback'
});

var scopes = ['user-read-private', 'streaming', 'user-modify-playback-state', 'user-read-playback-state', 'user-read-currently-playing', 'playlist-read-private'];
var state = 'not-sure-what-this-is';

// Create the authorization URL
var authorizeURL = spotifyApi.createAuthorizeURL(scopes,state);
console.log(authorizeURL);
