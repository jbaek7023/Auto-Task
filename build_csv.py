with open('webtoon.csv', 'wt', encoding='utf8') as f:
    f.write(lines)

import csv

rows = [
    ['월요웹툰', '화요웹툰', '수요웹툰', '목요웹툰', '금요웹툰', '토요웹툰', '일요웹툰'],
    ['신의 탑', '마음의소리', '고수', '기기괴괴', '덴마', '호랑이형님', '열럽전사'],
    ['귀전구담', '노블레스', '퍼미스미션', '하루 3컷', '테러맨', '부활남', '다이스'],
    ['히어로메이커', '하이브', 'DEY 호러채널', '마술사', '오즈랜드', '유미의세포들', '조선왕조실톡'],
]

# Write lists
with open('webtoon.csv', 'wt', encoding='utf8') as f:
    writer = csv.writer(f) #f, delimeter='|'
    writer.writerows(rows)

# Write dict
with open('webtoon_dictwriter.csv', 'wt', encoding='utf8') as f:
    fieldnames = ['last_name', 'first_name']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    # 1 Row를 쓸 때
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

    # 다수 Row를 쓸 때
    writer.writerows([
        {'first_name': 'Lovely', 'last_name': 'Spam'},
        {'first_name': 'Wonderful', 'last_name': 'Spam'},
    ])

# Read
with open('webtoon.csv', 'rt', encoding='utf8') as f:
    print(f.read())

'''
Issue : Incoding Problem
    Company uses Excel.

'''
