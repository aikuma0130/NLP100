import re

def extract_category(text):
    category_pattern = re.compile('\[\[Category:[^\]]+\]\]')
    return "\n".join(category_pattern.findall(text))

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_category(text))
