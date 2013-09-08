OkCupid
=======

This script allows you to send multiple messages on OkCupid to random users

##Installation

You must have python 2.7 and pip installed.
Use pip to install the following libraries:

```bash
pip install requests
pip install BeautifulSoup
```

Once you have cloned the repo you must edit queries.json and replace the value for "queryurl" with a vaild match url from your account on okcupid.com. Simply login, click "Matches" in the sidebar and adjust the search critera to you liking. Then paste the url into your queries.json file.
Here is how a valid queries.json may look:

```json
[
    {
        "name":  "Default Search",
        "queryurl":  "http://www.okcupid.com/match?filter1=0,34&filter2=2,18,35&filter3=3,50&filter4=5,31536000&filter5=1,1&filter6=35,0&filter7=25,4000,10000&locid=0&timekey=1&matchOrderBy=SPECIAL_BLEND&custom_search=0&fromWhoOnline=0&mygender=m&update_prefs=1&sort_type=0&sa=1&using_saved_search=",
        "filepath":  "./Lists/Default.txt",
        "id":  1,
        "filterout":  [
                          "./Lists/SentAMessage.txt",
                      ]
    }
]
```

Replace the two example queries in the file with urls of your choice or delete or add as many queries as you would like. NOTE: you MUST have a comma between multiple queries for it to be a valid json format. Like this:

```json
[
    {
        "name":  "Example 1",
        "queryurl":  "http://www.okcupid.com/",
        "filepath":  "./Lists/Example1.txt",
        "id":  1,
        "filterout":  [
                          "./Lists/SentAMessage.txt",
                          "./Lists/AlreadyMessagedBack.txt"
                      ]
    },
    {
        "name":  "Example",
        "queryurl":  "http://www.okcupid.com/",
        "filepath":  "./Lists/Example2.txt",
        "id":  3,
        "filterout":  [
                          "./Lists/SentAMessage.txt",
                          "./Lists/AlreadyMessagedBack.txt"
                      ]
    }
]
```
