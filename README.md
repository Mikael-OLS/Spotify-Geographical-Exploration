# Worlds Most Popular Music(Week 26) - An Exploration # 
## Table of Contents
1. [ Goals ](#Goal)
2. [ Summary Statistics ](#Summarystat)
 01.  [ Variable exploration ](#Variable)
 02.  [ Geographical exploration ](#Geographical)
3. [ Summary ](#Summary)
4. [ Legality ](#Legality)

<a name="Goal"></a>
## Goals
Whether I am on the train, the bike, coding or even doing anything at all - I listen to music. However, in the last couple of years when Spotify shows me my most listen to songs, I have realised that the songs are almost 100% from Sweden, the United States or the UK. This has peeked my interest in exploring music from around the world and to see if there is any difference. For example, is the popular music in Argentina similar to the popular music in Denmark. If no, in what patterns are they different? The goals of this project are:

* Which genres are the most popular? 
* Explore the popularity of different genres around the globe.
* Explore the difference in popular music around the globe.

<a name="Summarystat"></a>
## Summary Statistics
The Spotify API was used to scrape data of the 50 most popular tracks from 62 countries. However, only one african country is included in the dataset since I could not find any playlist in spotify from the other african countries. The dataset used ended up including data from 3100 songs.
<a name="Variable"></a>
### Variable exploration
First, let's see how the variables behave

![ability](https://user-images.githubusercontent.com/62875997/86040923-238a5700-ba45-11ea-8dd5-8cd1f2eb5018.png)

![genre](https://user-images.githubusercontent.com/62875997/86040958-34d36380-ba45-11ea-959d-7100b24d8a4e.png)

As one can see non of the variables looks normal. The genre-variables does not have any outliers, whilst the other variables have some. Now that we know the data better, let's apply a geographical dimension in the exploration.
<a name="Geographical"></a>
### Geographical exploration
![Skärmklipp 2020-06-24 21 06 55](https://user-images.githubusercontent.com/62875997/86041172-909dec80-ba45-11ea-82d5-a3ffd457735b.png)

Pop is by far most popular in Asia and least in South America.
![Skärmklipp 2020-06-24 21 07 18](https://user-images.githubusercontent.com/62875997/86041188-9398dd00-ba45-11ea-80e1-4ede7b403504.png)

Even though latin is one of the three most popular genres (see notebook), it is almost only popular in South America and Spain. This is interesting since many hit song nowadays are at least latin inspired. 

![Skärmklipp 2020-06-24 21 07 08](https://user-images.githubusercontent.com/62875997/86041181-93004680-ba45-11ea-8f8a-1b18209a6402.png)

Hip Hop has the biggest spread, it seems like it is either very popular or not all.

![Skärmklipp 2020-06-24 21 07 26](https://user-images.githubusercontent.com/62875997/86041192-94317380-ba45-11ea-81f7-38aa123c1c18.png)
![Skärmklipp 2020-06-24 21 07 34](https://user-images.githubusercontent.com/62875997/86041198-9562a080-ba45-11ea-8fb7-1d3e6203f52f.png)
![Skärmklipp 2020-06-24 21 07 41](https://user-images.githubusercontent.com/62875997/86041202-95fb3700-ba45-11ea-82de-5c4dba0985eb.png)

When it comes to the attributes, Asia (except Russia) has the lowest energy- and danceability level and the highest acousticness level. Central and South America have the highest danceabaility. As an outlier, Russia has the by far highest energy level. Except the observation about Russia, all the three abilities seems to correspond to the most popular genre in the region. For example, both the genre latin and danceabaility are most popular in Central and South America. This is probably due to the danceabaility being a key in the genre latin.
<a name="Summary"></a>
## Summary 
So what can we take with us from this exploration? Mainly that the popularity of genres differs vastly, probably more than you expect. Another observation is that the attributes seems to be determined almost exclusively by the popular genres and not by the geographical region. 
<a name="Legality"></a>
## Legality
This is a personal project made for non-commercial use ONLY and will not be used to generate any promotional or monetary value for me.

This project uses the Spotify API, and terms and conditions are found here: https://developer.spotify.com/terms/
