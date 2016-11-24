import re

def extract_template(text):
    basic_pattern = re.compile('{{基礎情報.*?\n\|(.*?)\n}}', re.DOTALL)
    result = {}
    for i in basic_pattern.findall(text):
        for j in i.split('\n|'):
            key = j.split(' = ')[0].lstrip()
            value = j.split(' = ')[1].rstrip()
            if key not in result:
                value = removal_emphasis(value)
                value = removal_internal_link(value)
                value = remove_ref(value)
                value = removal_template(value)
                result[key] = value
    return result

def removal_emphasis(text):
    max_emphasis_pattern = re.compile("'''''([^']+?)'''''", re.DOTALL)
    mid_emphasis_pattern = re.compile("'''([^']+?)'''", re.DOTALL)
    emphasis_pattern = re.compile("''([^']+?)''", re.DOTALL)
    text = max_emphasis_pattern.sub('\g<1>', text)
    text = mid_emphasis_pattern.sub('\g<1>', text)
    text = emphasis_pattern.sub('\g<1>', text)
    return text

def removal_internal_link(text):
    internal_link_pattern = re.compile("\[\[([^\\]\\|]+?)\]\]", re.DOTALL)
    internal_link_with_string_pattern = re.compile("\[\[([^\\]\\|]+?)\|([^\\]]+?)\]\]", re.DOTALL)
    internal_link_with_two_string_pattern = re.compile("\[\[([^\\]\\|]+?)\|([^\\]\\|]+?)\|([^\\]]+?)\]\]", re.DOTALL)
    text = internal_link_pattern.sub('\g<1>', text)
    text = internal_link_with_two_string_pattern.sub('\g<3>', text)
    text = internal_link_with_string_pattern.sub('\g<2>', text)
    return text

def removal_template(text):
    template_pattern = re.compile("{{([^}\\|]+?)}}", re.DOTALL)
    template_with_two_string_pattern = re.compile("{{([^}\\|]+?)\|([^}\\|]+?)\|([^}]+?)}}", re.DOTALL)
    template_with_string_pattern = re.compile("{{([^}\\|]+?)\|([^}\\|]+?)}}", re.DOTALL)
    text = template_pattern.sub('\g<1>', text)
    text = template_with_two_string_pattern.sub('\g<3>', text)
    text = template_with_string_pattern.sub('\g<2>', text)
    return text

def remove_ref(text):
    ref_one_tag_pattern = re.compile("<ref[^<]*?/>", re.DOTALL)
    ref_pattern = re.compile("<ref.*?>.*?</ref>", re.DOTALL)
    text = ref_one_tag_pattern.sub('', text)
    text = ref_pattern.sub('', text)
    return text

if __name__ == '__main__':
    import sys
    sys.path.append('../20/')
    from extract_country import extract_country
    
    text = extract_country('../jawiki-country.json.gz', 'イギリス')
    print(extract_template(text))
