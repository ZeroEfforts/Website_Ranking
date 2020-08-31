from googlesearch import search


def gsearch(query_, tld_='com', lang_='en', num_=100, start_=0, stop_=100, pause_=2):
    if pause_ < 2:
        pause_ = 2
    try:
        return list(search(query=query_, tld=tld_, lang=lang_,
                           num=num_, start=start_, stop=stop_, pause=pause_))

    except Exception as err:
        return err
