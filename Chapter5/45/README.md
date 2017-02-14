# Exec UNIX Commands

* 頻出単語抽出
```
# cat case_pattern_of_verbs.txt |awk '{print $1}' |sort |uniq -c |sort > verbcount.txt
```

* 「する」「見る」「与える」の動詞の格集計
```
# cat case_pattern_of_verbs.txt |grep ^'する\t' |awk -F '\t' '{print $2}' |tr ' ' '\n' |sort |uniq -c |sort > suru_case.txt
# cat case_pattern_of_verbs.txt |grep ^'見る\t' |awk -F '\t' '{print $2}' |tr ' ' '\n' |sort |uniq -c |sort > miru_case.txt
# cat case_pattern_of_verbs.txt |grep ^'与える\t' |awk -F '\t' '{print $2}' |tr ' ' '\n' |sort |uniq -c |sort > ataeru_case.txt
```
