import re

def extract_chapter(text):
    chapter_pattern = re.compile('^==([^=]+)==$')
    chapter_number_pattern = re.compile('^(=*)')
    chapter_name_pattern = re.compile('^=*([^=][^=]*)=*$')
    result = []
    for line in text.split('\n')[:-1]:
        for chapter in chapter_pattern.findall(line):
            number = len(chapter_number_pattern.search(chapter).group(1)) + 1
            name = chapter_name_pattern.findall(chapter)[0]
            result.append({ "name": name, "number": number })
    #return result
    return "\n".join([ str(data["number"]) + " " + data["name"] for data in result ])

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_chapter(text))
