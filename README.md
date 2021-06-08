# framestore

This is a simple aplication that fetches data from social media accounts, stores it in an SQLite database for later use and presents it to the user using the Django template engine.

-At /social-rss/setup/create you can add social media accounts to the database under a username, the app currently supports youtube and twitter.<br />
-At /social-rss/"your-username" you can check the feed of your account, the first requests to this endpoint usually takes about 30 seconds because the database is being created.

-The sample html output/pictures are available at the "samples" folder.
  
# Sample Pictures

<img src="https://github.com/LFBianchi/framestore/blob/main/samples/sample_01.png">

<img src="https://github.com/LFBianchi/framestore/blob/main/samples/sample_02.png">
