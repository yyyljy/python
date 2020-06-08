# 04_dict_and_set
# 1. dictionary
# key, value로 이루어져있음
dict_a = {}
dict_b = dict()
# key가 중복이 불가능하다.
dict_a = {'삼성':100, '역삼':50, '선릉':30}
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

print(dict_a['삼성'])
print(dict_a.get('삼성'))

# .get과 [] 접근 차이점
dict_a = {'삼성':100, '역삼':50}
print(dict_a.get('선릉'))
#print(dict_a.['선릉'])

# 2. set
# set는 순서가 없이 저장된다.
# 중복이 없다
set_a = {1,3,2}
set_b = set()
set_c = {3,6,8}
print(set_a-set_c)
print(set_a | set_c)
print(set_a & set_c)

list_a = [1,1,1,1]
print(list(set(list_a)))

string = "immutable"
list_a = ['immutable?','real?']
list_b = list_a
print(string[0])
print(list_a[0])
#string[0] = 'a'
list_a[0] = 'mutable'

print(list_a)
