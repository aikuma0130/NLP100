import re

def extract_template(text):
    basic_pattern = re.compile('{{基礎情報.*?\n\|(.*?)\n}}', re.DOTALL)
    result = {}
    for i in basic_pattern.findall(text):
        for j in i.split('\n|'):
            key = j.split(' = ')[0].lstrip()
            value = j.split(' = ')[1].rstrip()
            if key not in result:
                result[key] = removal_markup(value)
    return result

def removal_markup(text):
    max_emphasis_pattern = re.compile("'''''([^']+?)'''''", re.DOTALL)
    mid_emphasis_pattern = re.compile("'''([^']+?)'''", re.DOTALL)
    emphasis_pattern = re.compile("''([^']+?)''", re.DOTALL)
    text = max_emphasis_pattern.sub('\g<1>', text)
    text = mid_emphasis_pattern.sub('\g<1>', text)
    text = emphasis_pattern.sub('\g<1>', text)
    return text

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_template(text))
