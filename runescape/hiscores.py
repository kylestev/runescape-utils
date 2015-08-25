import json
import requests
from itertools import izip


STAT_NAMES = [
    'Overall', 'Attack', 'Defence', 'Strength', 'Constitution', 'Ranged',
    'Prayer', 'Magic', 'Cooking', 'Woodcutting', 'Fletching', 'Fishing',
    'Firemaking', 'Crafting', 'Smithing', 'Mining', 'Herblore', 'Agility',
    'Thieving', 'Slayer', 'Farming', 'Runecrafting', 'Hunter', 'Construction',
     'Summoning', 'Dungeoneering', 'Divination'
]

TRIPLET_KEYS = ['Rank', 'Level', 'XP']

URL_HISCORES = 'http://services.runescape.com/m={}/index_lite.ws'


class LiteHiscoresParser(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def _fetch(self, username):
        r = requests.get(self.endpoint, params={'player': username})

        if r.status_code != 200:
            message = 'Unable to retrieve stats for {} using endpoint {}'
            raise Error(message.format(username, self.endpoint))

        return self._transform(r.content)

    def _transform(self, response):
        for triplet in response.split():
            pieces = map(int, triplet.split(','))
            if len(pieces) == 3:
                yield dict(izip(TRIPLET_KEYS, pieces))


    def lookup(self, username):
        return dict(izip(STAT_NAMES, self._fetch(username)))


class RuneScapeHiscores(LiteHiscoresParser):
    def __init__(self):
        hiscores_url = URL_HISCORES.format('hiscore')
        super(RuneScapeHiscores, self).__init__(hiscores_url)


class RuneScapeIronmanHiscores(LiteHiscoresParser):
    def __init__(self):
        hiscores_url = URL_HISCORES.format('hiscore_ironman')
        super(RuneScapeIronmanHiscores, self).__init__(hiscores_url)


class RuneScapeHardcoreIronmanHiscores(LiteHiscoresParser):
    def __init__(self):
        hiscores_url = URL_HISCORES.format('hiscore_hardcore_ironman')
        super(RuneScapeHardcoreIronmanHiscores, self).__init__(hiscores_url)


class OldSchoolHiscores(LiteHiscoresParser):
    def __init__(self):
        hiscores_url = URL_HISCORES.format('hiscore_oldschool')
        super(OldSchoolHiscores, self).__init__(hiscores_url)


class OldSchoolIronmanHiscores(LiteHiscoresParser):
    def __init__(self):
        hiscores_url = URL_HISCORES.format('hiscore_oldschool_ironman')
        super(OldSchoolIronmanHiscores, self).__init__(hiscores_url)


class OldSchoolUltimateIronmanHiscores(LiteHiscoresParser):
    def __init__(self):
        hiscores_url = URL_HISCORES.format('hiscore_oldschool_ultimate')
        super(OldSchoolUltimateIronmanHiscores, self).__init__(hiscores_url)


class Hiscores:
    oldschool = OldSchoolHiscores
    oldschool_ironman = OldSchoolIronmanHiscores
    oldschool_ultimate = OldSchoolUltimateIronmanHiscores
    runescape = RuneScapeHiscores
    runescape_ironman = RuneScapeIronmanHiscores
    runescape_hardcore_ironman = RuneScapeHardcoreIronmanHiscores
