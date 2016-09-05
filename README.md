This is a simple script that utilizes the Firefox selenium
webdriver to snoop all cookies including the http only ones.

The problem with http only cookies is that they are not retrievable
by the ```document.cookie``` javascript object which makes them not
accessible to the selenium webdriver.

The httponly cookies are on the other hand retrievable using the cookies
tab in the debug console of Firefox. Unfortunately there is no easy way to
programmaticaly retrieve them in the context of a selenium script.

The solution I found at work was to actually go into the implementation details
of the session store Firefox uses.

What the code of the script does is it finds where the current Firefox webdriver
session storage is and it parses the json file that actually stores the data.
This is in fact the mechanism that Firefox uses to restore a session.

The only drawback is that a cookie may not be immediately available in this
json file. The most probable cause of this would be that Firefox does not
write the session file on every session state change but instead has a timer
to periodically update this file.

If you are looking for a particular cookie to be present you could implement
a small busy waiting loop to wait for the presence of the cookie in question.
