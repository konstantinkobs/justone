# JUST ONE

My implementation of Just One, a German word based card game.
This "game" basically is just showing random words.
You swipe from right to left on your phone or press the right arrow button to go through the list.
You can find more information about this game [here](https://asmodee.de/just-one).

## Playing with multiple people

You can play with multiple people by sending them the link that is generated when the page is opened or adding a hashtag at the end of the URL, e.g. `#123456789` or `#thisgameisawesome`.
Given the same link, the order of words should be the same for everyone.
This way, each player can go to the same next word.
Don't forget to catch up if it was your turn. :smile:
Please remove or modify the hashtags if you want to play a new round with a new word order.

## Generating Word List

1. Take images of all cards. I photographed 16 cards at once, layed out in a 4 by 4 grid
2. Put them into the folder `wordlist/images`
3. Install the Python dependencies in `wordlist/requirements.txt`
4. Go into the `wordlist` folder and run `python3 generate_wordlist.py`
5. Go through the generated list `wordlist.txt` and correct any wrong words. You can also add new words or modify them in the file, if you want
