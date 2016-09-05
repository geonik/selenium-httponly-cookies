#!/usr/bin/env python3

from selenium import webdriver


import json
import os.path


def get_cookies(driver):
    profile_path = driver.firefox_profile.path
    recover_json_path = os.path.join(
        profile_path,
        'sessionstore-backups',
        'recovery.js'
    )

    with open (recover_json_path, 'rt') as fh:
        data = json.load(fh)

    cookies = []

    # Debug print
    # print('data is {0}'.format(json.dumps(data, indent=4)))

    # Cookies are retained for active and closed windows
    if 'cookies' in data['windows'][0]:
        window = data['windows'][0]

        # Debug print
        # print(json.dumps(window, indent=4))

        if 'cookies' in window:
            cookies.extend(window['cookies'])
    return cookies

def main():
    driver = webdriver.Firefox()
    # Open a site to get some cookies set
    driver.get('https://www.amazon.com')


    cookies = get_cookies(driver)
    print('Retrieved cookie list \n{0}'.format(json.dumps(cookies, indent=4)))

    driver.close()


if __name__ == '__main__':
    main()
