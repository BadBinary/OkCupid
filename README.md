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

Once you have cloned the repo you must edit queries.json and replace the value for "queryurl" with a vaild match url from your account on okcupid.com. Simply login, click "Matches" in the sidebar and adjust the search critera to you liking. NOTE: for the time being you MUST set "Order by" to "Totally Random", this helps to get as many matches as possible, soon this will not be needed when this script is built out further. Paste the url into your queries.json file.
Here is how a valid queries.json may look:

```json
[
    {
        "name":  "Default Search",
        "queryurl":  "http://www.okcupid.com/match?filter1=0,34&filter2=2,18,35&filter3=3,50&filter4=5,31536000&filter5=1,1&filter6=35,0&filter7=25,4000,10000&locid=0&timekey=1&matchOrderBy=RANDOM&custom_search=0&fromWhoOnline=0&mygender=m&update_prefs=1&sort_type=0&sa=1&using_saved_search=",
        "filepath":  "./Lists/Default.txt",
        "filterout":  [
                          "./Lists/SentAMessage.txt",
                      ]
    }
]
```

Replace the two example queries in the file with urls of your choice or delete or add as many queries as you would like. NOTE: you MUST have a comma between multiple queries (look at the comma after the "}" symbol below) for it to be in valid json format. Like this:

```json
[
    {
        "name":  "Example 1",
        "queryurl":  "http://www.okcupid.com/match?blah=blah&more-search-parameters-here",
        "filepath":  "./Lists/Example1.txt",
        "filterout":  [
                          "./Lists/SentAMessage.txt",
                          "./Lists/Example2.txt"
                      ]
    },
    {
        "name":  "Example 2",
        "queryurl":  "http://www.okcupid.com/match?blah=blah&then-some-more-search-parameters-here",
        "filepath":  "./Lists/Example2.txt",
        "filterout":  [
                          "./Lists/SentAMessage.txt",
                          "./Lists/Example1.txt"
                      ]
    }
]
```

Your "filepath" must be a unique filepath it doesn't matter if it doesn't exist the list will be created for you. The "filterout" attribute is any userlist you want not to be a part of this list. This script automatically makes a list of users you've sent a message to already ("./Lists/SentAMessage.txt") so I would suggest putting in that list for "filterout" as well as any other list you may have running already.

Once you are done editing your queries.json cd to the cloned directory on your local machine run the following:

```Python
python makelists.py
```

This will create your lists of users to send messages to and serve as a way to update your lists when new users sign up. You may consider a scheduled task or cron job to update your lists for you.

Now in the folder "Messages" you must add txt files to be your message(s) you want to send out. The filename does not matter. Place each message you want to use in an individual txt file of its own and the script will pick one of the messages at random to send out. If you have just one txt file it will send that message every time.
To send your messages run the following:

```Python
python automatemessages.py "./Lists/Default.txt" 100
```

The first argument is the path to the list you want to pull usernames from and the second argument is how many messages to send.
So in the example above you would be sending 100 messages to users from the list "./Lists/Default.txt"


