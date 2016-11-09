import re

def extract_mediafile(text):
    mediafile_pattern = re.compile(':(.*?jpe*g)\|')
    return '\n'.join([ mediafile for mediafile in mediafile_pattern.findall(text) ])

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_mediafile(text))
