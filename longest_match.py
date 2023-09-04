# 방법2. sorting하지 않고 치환
dictionary = {"ab":"xxx", "cde":"yyy", "rr":"QQ", "cdefgh":"zzz", "z":"X"}
src = "qqq abcde rrr abcdefghz"
isReplaced = [0]*len(src)          # 치환 여부 확인 리스트

# key 기준으로 내림차순 정렬
new_dict = dict(sorted(dictionary.items(), key=lambda x: len(x[0]), reverse=True))

result = src

max_len = len(max(dictionary, key=len))
print(max_len)


for i in range(max_len, 0, -1):        
    substring=""

    for j in range(len(result)):
        
        print(f'result: {len(result)} {result}')
        print(f'isReplaced: {len(isReplaced)} {isReplaced}\n')
        print('j: ', j)

        substring = result[j:j+i]
        
        print(substring)

        if (isReplaced[j] == 0) and (substring in dictionary):
            key = substring
            value = dictionary[key]
            print('***** key == substring *****')
            result = result[:j] + value + result[j+i:]
            print(f'"{key}"를 "{value}"로 교체 후 result: {result}\n')
            isReplaced[j:j+i]=[1]*len(key)         # 치환 여부 true(1)로 변경
            
            # isReplaced resize - key와 value의 길이가 다를 때, 
            if len(key) > len(value):
                isReplaced = isReplaced[:j+i-len(key)+len(value)] + isReplaced[j+i:]
                print(f'isReplaced 수정(축약): {isReplaced} 길이:{len(isReplaced)}')
            elif len(key) < len(value):
                print('insert 전 isReplaced ', isReplaced)
                isReplaced[j+i:j+i] = [1]*(len(value)-len(key))
                print(f'insert 후 isReplaced: {isReplaced} 길이:{len(isReplaced)}')
            substring = ""
            break
            
        #if (substring not in dictionary) and len(substring) == max_len:
        #    break

    else:
        j=0

print(result)