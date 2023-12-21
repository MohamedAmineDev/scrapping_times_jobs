import re


def fetch_enterprise_name(soup):
    value = soup.find('ul', class_='jd-comp-main')
    if value is not None:
        enterprise_name_element = value.find('span', class_='basic-info-dtl')
        if enterprise_name_element is not None:
            return enterprise_name_element.text.strip()
    return 'Unknown'


# card_travel
def fetch_address(soup):
    icons_element = soup.find_all('li', class_='')
    for icon in icons_element:
        if 'location_on' in icon.text:
            return icon.get('title')
    return ''


def format_date(value):
    res = ''
    i = 0
    while i < len(value) - 1:
        if value[i] in '0123456789':
            if value[i + 1] in 'abcdefghijklmnopqrstuvwxyz':
                res = f'{res}{value[i]} '
            else:
                res = f'{res}{value[i]}'
            i = i + 1
            continue
        if value[i] in 'abcdefghijklmnopqrstuvwxyz':
            if value[i + 1] in 'abcdefghijklmnopqrstuvwxyz':
                res = f'{res}{value[i]}'
            else:
                res = f'{res}{value[i]} '
        i = i + 1
    return res


def fetch_experience(soup):
    icons_element = soup.find_all('li', class_='')
    for icon in icons_element:
        if 'card_travel' in icon.text:
            value = icon.text
            value = value.replace('\t', '').replace('\n', '').replace(' ', '').split('card_travel')[1]
            return format_date(value)
            # return re.sub(r'(\d+)([a-zA-Z]+)', r'\1 \2', value)
    return ''
