# WebzScrape

## OOP Project; Web scraper for Aamzon that allows multiple searches and returns unorganized, listed information of products matching search.

### Issues:

The search algorithm is given, based on the search for "Tent". Therefore the html format of other data pertaining to other searches may not be the same, and will throw an error. Implemented a try: clause for error, should dispute search and return for another input.

Following further look over the code and other similar work found online, I realize my work may be lacking in some more professional and practical ways. 
I will happily take advice/critiques.

|--------------------------------------------------|
                
Current file is based on xpath of the search bar and submit-search bar at www.amazon.com. This could lead to issues with finding said buttons.
I have the data being re-written into a json file/form for absolutely no reason. I thought it'd be interesting to use and realized it is no different from a list of dictionaries. Personally with the list, I could wrap the text so it'll be printed easier on the eyes. Hopefully to get done in next update.

|--------------------------------------------------|

I got new directory added for my new laptop, but still cannot find the best sellers page. Also ran into issue with amazon knowing I'm a bot and couldn't figure the issue out. It may have been because I was running the script so often when I was figuring out why the chrome driver wasn't working, but I got it on my PATH and also did get amazon to let me on once, even after all the runs, and I just got it to do it once just now too. I guess if I use the scraper alot it'll tip off amazon, but I don't know how many times.

|--------------------------------------------------|
