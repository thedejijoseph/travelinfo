21 02 2021

Starting work on this stuff after all.

23 02 2021
I created a script to populate the database with dummy data, but it seems that won't cut it for tests.

I'm writing another with a small collection of the ones I know and will test with.

24 02 2021; 0048
server.py contains stuff I describe as "as simple as simple gets" and that is the case.
My priority here is getting something that works: i.e responds to requests online. I need to mess around with Azure's hosting, as well as get the basics of connecting a bot service to my api.. we'll move on from there.

03 03 2021; 1959
I built and deployed the terminal connecting thing. It's not done yet, in terms of design and functionality.
Working on the chatbot side of things now. It looks as simple as sourcing example messages users might communicate with but it is also a bit more involved than that.

**08 03 2021; 1509**

More like a status update.

For a couple of days now, getting started with building the bot's logic has been hectic. 

There are couple of options to build this "bot logic".

1. Microsoft's Azure Bot Service: elusive
2. Bot Framework Composer: an installable GUI.
3. Bot Framework SDK: language specific libraries.

**One.**

I haven't decided what they actually mean by that, how to access it and how to use it

**Two.**

Downloaded source code. Even though their README says node v10 would build it, it's not building it. Need to upgrade node to v12 or v14. Something with nodejs.org's repo is slowing download so bad, it's failing via nvm and npm's n module. Trying a manual download and install now but that's still very slow.

**Three.**

Installed Python's libraries and some sample code. Started sample code as a server. Need the Bot Framework Emulator to play around with that but it's not installing. Something about libsecret-1-dev being needed and apt-get install is failing cause of some unreachable IP. Plus there's no API design Schema for me to manually check the server out.

Honestly, at this point, I'm tired.

Will turn things off, take a break and come back.

08 04 2021; 2156

Internet connection improved, node v14 is installed and Composer is being built.

09 04 2021; 1025

After a couple of failed builds yesterday, I got the Composer up and running. So, I guess my break paid off. On the other hand, I used my break to finally get the Browse part of the project up and running. Will put some finishing touches to that and come back here.

09 04 2021; 2331

I finished building what seems to be a usable app for data entry. Going back to figuring out this chatbot thing.

Yh. I didn't mention that, depending on what I find this time around, this project might not be any more useful. Or atleast, i'd be wrapping it into Azure's specification..

18032021; 2015

After all that time away, I finally have some grasp on Azure's Cognitive Services ecosystem, and that includes setting up their components including: Python SDK, Composer, and Emulator.

I'm not sure what I'll be building the bot with yet (Composer or SDK) but I need to put finishing touches to this "query resolver" if I'm to make progress on that end.
