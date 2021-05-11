
# --- 1 ---
name1 = 'ねずこ'
name2 = 'ぜんいつ'
print('{}と{}は仲間です'.format(name1, name2))

# --- 2 ---
name2 = 'むざん'
print('{}と{}は仲間ではありません'.format(name1, name2))

# --- 3 ---
name = ["たんじろう","ぎゆう","ねずこ","むざん"]
name.append('ぜんいつ')

# --- 4 ---
for obj in name:
    print(obj)

# --- 5 ---
def names():
    print('ねずこ')

names()

# --- 6 ---
def character(character):
    if character in name:
        print('{}はnameに含まれます'.format(character))
    else:
        print('{}はnameには含まれていません'.format(character))

character('ねずこ')








