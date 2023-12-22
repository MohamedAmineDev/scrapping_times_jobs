def fetch_enterprise_name(soup):
    value = soup.find('ul', class_='jd-comp-main')
    if value is not None:
        enterprise_name_element = value.find('span', class_='basic-info-dtl')
        if enterprise_name_element is not None:
            return enterprise_name_element.text.strip().replace('.', '').replace(',', '')
    return 'Unknown'


def fetch_address(soup):
    icons_element = soup.find_all('li', class_='')
    for icon in icons_element:
        if 'location_on' in icon.text:
            return icon.get('title')
    return 'Unknown'


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
    return 'Unknown'


def fetch_title(soup):
    title_element = soup.find('h1', class_='jd-job-title')
    if title_element is not None:
        return title_element.text.strip()
    return 'Unknown'


def fetch_date(soup):
    date_element = soup.find_all('ul', class_='top-job-insight')
    if date_element is not None:
        li_element = date_element[0].find_all('strong')
        if li_element is not None:
            return li_element[1].text.strip().replace(',', '')
    return 'Unknown'


def fetch_qualification(soup):
    span_elements = soup.find_all('span', class_='basic-info-dtl')
    for span in span_elements:
        ul_element = span.find('ul')
        if ul_element is not None:
            li_element = ul_element.find('li')
            if li_element is not None:
                return li_element.text.strip()
    return 'Unknown'


def fetch_skills(soup):
    skill_elements = soup.find_all('span', class_='jd-skill-tag')
    res = ''
    for skill in skill_elements:
        if skill is not None:
            a = skill.find('a')
            if a is not None:
                if res == '':
                    res = f'{a.text.strip()}'
                else:
                    res = f'{res},{a.text.strip()}'
    return res
