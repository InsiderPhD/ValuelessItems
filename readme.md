```
     __                      _                                               |
  /\ \ \___  ___  _ __   ___| |_ ___                                         |
 /  \/ / _ \/ _ \| '_ \ / _ \ __/ __|                                        |
/ /\  /  __/ (_) | |_) |  __/ |_\__ \                                        |
\_\ \/ \___|\___/| .__/ \___|\__|___/                                        |
                 |_|                                                         |
             _            _                  _____ _                         |
 /\   /\__ _| |_   _  ___| | ___  ___ ___    \_   \ |_ ___ _ __ ___  ___     |
 \ \ / / _` | | | | |/ _ \ |/ _ \/ __/ __|    / /\/ __/ _ \ '_ ` _ \/ __|    |
  \ V / (_| | | |_| |  __/ |  __/\__ \__ \ /\/ /_ | ||  __/ | | | | \__ \    |
   \_/ \__,_|_|\__,_|\___|_|\___||___/___/ \____/  \__\___|_| |_| |_|___/    |                                                    
   __                                _   _____            _                  |
  /__\ ___ _ __ ___   _____   ____ _| | /__   \___   ___ | |                 |
 / \/// _ \ '_ ` _ \ / _ \ \ / / _` | |   / /\/ _ \ / _ \| |                 |
/ _  \  __/ | | | | | (_) \ V / (_| | |  / / | (_) | (_) | |                 |
\/ \_/\___|_| |_| |_|\___/ \_/ \__,_|_|  \/   \___/ \___/|_|                 |
(updated for 2024)                                                           |
                                                                             |
-----------------------------------------------------------------------------+
```

Fork of https://github.com/wschneider/ValuelessItems

Hello this is a fork of popular Neopets extension ValuelessItems to update it to 2024

- Neopets has moved to https so this has too! manifest.json has been updated to https
- The prices in `itemsheet.csv` have been refreshed from JellyNeo
- To help keep this up to date a new script called `generate_csv_jelly.py` can be used to automatically refresh the tool from jellyneo with your own maxprice
- If you use [SDB Junk Highlighter](https://github.com/mag-fish/laughing-octo-fortnight/blob/master/junk-highlighter) you can refresh that script by copying the code from `sdb_defwords.txt` and replacing line 33-1958 of that script
- If you use [SDB Junk Highlighter](https://github.com/mag-fish/laughing-octo-fortnight/blob/master/junk-highlighter) AND you want to refresh that script too you can use `generate_sdb.py` to automatically update it too
- If you want to tweak this script yourself I've provided an example jellyneo search page for reference in `jellyneo.html`

Instructions
0. If you are reading this file, you have either found, or downloaded the codes from github. If not, you will want to visit the website listed below and click the "Download Zip" button on the lower right side. Unpack it somewhere on your computer
1. (Optional) If you want to refresh the prices you'll need to download Python and [requests](https://pypi.org/project/requests/) and [beautiful soup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup) via pip using `python -m pip install requests` and `python -m pip install beautifulsoup4`. You can then run `generate_csv_jelly.py` by default this script will highlight any items with a neopoint value of less than 100NP, if you want to change this adjust the "max_price" value on line 8. You
2. If you are adding your own items to the list of items or you have refreshed the prices via the previous instruction, continue with this step. If you are not, proceed to step 3. Open `itemsheet.csv` with your favorite spreadsheet editor (or text editor, that works too). At the very end of the list, you can add any items you wish (as long as they are formatted so that one is on each line). When you save it you MUST be sure to save it as `itemsheet.csv`. Once you have saved it run the script `genscript.py`, which will generate a new `highlight.js` file. This file is your chrome extension.
3. Now you either have a self-generated (from Step 1) or the packaged `highlight.js` file. Open Google Chrome, and go to "chrome://extensions/" where you should select the "Load Unpacked Extension..." option. Navigate to where you unpacked the directory where you unpacked the download, and click "Ok".
4. (Optional) For [SDB Junk Highlighter](https://github.com/mag-fish/laughing-octo-fortnight/blob/master/junk-highlighter) users, if you refreshed the list of items yourself run the `generate_sdb.py` script. Copy all the text in `sdb_defwords.txt`, now go to the Tampermonkey dashboard using the extension settings, and find "SDB junk highlighter" click on the edit icon on the right (pencil writing icon), highlight all the text on line 33-1958, then paste the text from the `sdb_defwords.txt` file. Alternatively replace the userscript with `SDB junk highlighter-1.0.user.js` from the files.
5. Go to "http://www.neopets.com/quickstock.phtml". Any items that were listed in "itemsheet.csv" should be highlighted in green. As an economist, I recommend whole-heartedly that you discard these items, but do as you wish. Good Luck!


