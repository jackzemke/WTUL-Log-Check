## README

Current idea for workflow:
 - idea for passing in the songs is up in the air, see TODO
 - pass in link to a show and have flask or something parse out all of the song names w/ artist name 
 - figure out how to get the spotify track id for each track 
 - pass in to Spotify API's `get` function
    - includes a `popularity` attribute. rated from 0 to 100

TODO:
 - figure out how i want it obtain track ID. 
 - might be a smarter idea to have it run continuously in the background. might be better at getting around spotify's rate limits
    - can run it on this, which is basic html and continuously updated: [Link here](https://www.wtulneworleans.com/media/popupplayer.html)
 - just send an email when a song is played that has a popularity score above a certain threshold 
 - what threshold? need to check in with the station for that
 - how do i get it to run continuously in the background? 