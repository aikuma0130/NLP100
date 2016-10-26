import gzip
import json

def extract_country(jsonfile, country):
    with gzip.open(jsonfile, 'r') as f:
        for line in f:
            line = line.decode('utf-8')
            j = json.loads(line)
            if j['title'] == country:
                return j['text']

if __name__ == '__main__':
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(text)
