from runescape import hiscores

def hiscores_lookup(username, hiscore=hiscores.Hiscores.oldschool):
    if type(hiscore) == str:
        if hasattr(hiscores.Hiscores):
            hiscore = getattr(hiscores.Hiscores, hiscore)
    return hiscore().lookup(username)
