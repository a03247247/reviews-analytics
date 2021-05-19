data = []
count=0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count %100000 == 0:
            print(len(data))

print('檔案讀取結束,總共有', len(data),"筆資料")

sum_len = 0
for d in data:
    sum_len += len(d)  #sum_lem = sum_len + len(d)
    
print ('平均長度為', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有' ,len(new),'筆資料長度小於100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('共有', len(good), '比留言提到good')

wc = {}  #word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('您想搜尋的字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')

print('感謝使用本功能')