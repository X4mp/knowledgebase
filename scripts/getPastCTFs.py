#!/usr/bin/env python

#
# Run script and copy output to bottom of meetings.md
#

import re
import requests
from bs4 import BeautifulSoup

BASEURL = 'https://ctftime.org'
TEAMURL = '/team/8323'

# API (not usefull):
# * https://ctftime.org/api/v1/teams/8323/ --> not enough infos :(
# * https://ctftime.org/api/v1/events/212/ --> wrong numbers :(


def getNumberOfParticipatingTeams(ctf_url):
    team_html = requests.get(BASEURL + ctf_url).text
    soup = BeautifulSoup(team_html, 'html.parser')

    return soup.find_all('td', {'class': 'place'})[-1].string


def getPastCTFs():
    team_html = requests.get(BASEURL + TEAMURL).text
    soup = BeautifulSoup(team_html, 'html.parser')

    for year_data in soup.find_all('div', id=re.compile("rating_")):
        year = year_data.get('id')[7:]
        print '* %s' % year
        for ctf in year_data.find_all('tr'):
            cols = ctf.find_all('td')
            if len(cols) <= 0:
                continue
            ctf_place = cols[1].string
            ctf_name = cols[2].string.replace(year, '').strip()
            ctf_url = cols[2].find('a').get('href')
            ctf_participants = getNumberOfParticipatingTeams(ctf_url)
            print '  * %s <span class="discreet">(place %s of %s)</span>' % (ctf_name, ctf_place, ctf_participants)

if __name__ == '__main__':
    getPastCTFs()
