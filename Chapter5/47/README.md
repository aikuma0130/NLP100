# 実行UNIXコマンド
* コーパス中で頻出する述語（サ変接続名詞+を+動詞）
```
# python extract_verb_case_and_frame.py |awk '{print $1}' |sort |uniq -c |sort > frequent_predicates.txt
```

* コーパス中で頻出する述語と助詞パターン  
返事をする
```
# python extract_verb_case_and_frame.py |grep '返事をする' |awk -F'\t' '{print $2}' |tr ' ' '\n' |sort |uniq -c |sort > henji_frequent_particle.txt
```

挨拶をする
```
# python extract_verb_case_and_frame.py |grep '挨拶をする' |awk -F'\t' '{print $2}' |tr ' ' '\n' |sort |uniq -c |sort > aisatsu_frequent_particle.txt
```

話をする
```
# python extract_verb_case_and_frame.py |grep '話をする' |awk -F'\t' '{print $2}' |tr ' ' '\n' |sort |uniq -c |sort > hanashi_frequent_particle.txt
```
