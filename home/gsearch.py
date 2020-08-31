from googlesearch import search as search


def gsearch(query, tld='com', lang='en', num=100, start=0, stop=100, pause=2):
    if pause < 2:
        pause = 2
    try:
        s = search(query, tld='com', lang='en',
                   num=10, start=0, stop=1, pause=2)
        s=list(s)
        count = len(s)
        return count, s
    except Exception as err:
        return err
