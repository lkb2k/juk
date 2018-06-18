const url = require('url');
const SpotifyWebApi = require('spotify-web-api-node');

var spotifyApi = new SpotifyWebApi({
    clientId: 'f4e5e94a0eb84444af47c70ee85a8434',
    clientSecret: '8eed3a7e891d4641ae1dac67ecc3de84',
    redirectUri: 'http://localhost/callback'
});

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