import re

def extract_template(text):
    basic_pattern = re.compile('{{基礎情報.*?\n(|.*?)\n}}', re.DOTALL)
    field_pattern = re.compile('\|(.*?)\n\|', re.DOTALL)
    for i in basic_pattern.findall(text):
        for j in field_pattern.findall(i):
            print(j)

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_template(text))
