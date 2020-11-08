### Fun Stuff
* Modifying the user agent didn't work; Amazon still blocked the scraping
* Used **selenium** (web driver) instead
    * I could have used Safari but here's the Chrome driver: https://sites.google.com/a/chromium.org/chromedriver/home
* `\xa0` is the unicode for a _no break space_, which looks exactly like a white space, you can't really tell. To replace it with a white space in Python, use `replace(u'\xa0', u' ')`

