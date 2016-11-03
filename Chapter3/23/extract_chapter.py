import re

def extract_chapter(text, level=1, number=[]):
    chapter_pattern = re.compile('==(.*)==')
    chapter_level_pattern = re.compile('^=(=*)')
    chapter_name_pattern = re.compile('^=*([^=]+)=*$')
    result = []
    pre = 0
    chapter_index = [ 0 for i in range(5) ]
    for line in text.split('\n')[:-1]:
        if chapter_pattern.match(line):
            name = chapter_name_pattern.findall(line)[0].strip()
            level = len(chapter_level_pattern.search(line).group(1)) - 1

            chapter_index[level] = chapter_index[level] + 1
            for i, v in enumerate(chapter_index):
                if i > level:
                   chapter_index[i] = 0

            result.append({ "name": name, "number": ".".join( str(index) for index in chapter_index[:level+1]) })

    return '\n'.join([ "{0:<6}".format(data['number']) + " " + data['name'] for data in result ])

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_chapter(text))
