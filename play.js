var SpotifyWebApi = require('spotify-web-api-node');

var spotifyApi = new SpotifyWebApi();

spotifyApi.refreshAccessToken().then(function(data) {
    console.log('Retrieved data for ' + JSON.stringify(data.body));  
    spotifyApi.setAccessToken(data.body['access_token']);
    return spotifyApi.pause();
}).then(function(data) {    
    console.log('Retrieved data for ' + JSON.stringify(data.body));
  })
  .catch(function(err) {
    console.log('Something went wrong', JSON.stringify(err));
  });
