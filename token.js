require('dotenv').config()
const url = require('url');
const SpotifyWebApi = require('spotify-web-api-node');
const env = require('./env');

var spotifyApi = new SpotifyWebApi(env.spotify.credentials);

var redirectURL = url.parse(process.argv[2], true);
var code = redirectURL.query['code'];

console.log('CODE: '+code);

// First retrieve an access token
spotifyApi
  .authorizationCodeGrant(code)
  .then(function(data) {
    console.log('AUTH: '+data.body['access_token']);
    console.log('AUTH: '+data.body['refresh_token']);
  })
  .catch(function(err) {
    console.log('Something went wrong', JSON.stringify(err));
  });