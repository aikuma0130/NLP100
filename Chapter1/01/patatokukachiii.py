string = 'パタトカクシーー'

expected = 'パトクー'

result = string[0:7:2]

try:
    assert result == expected
    print('OK')
except:
    print('NG')
