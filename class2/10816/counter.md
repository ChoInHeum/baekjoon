# 1. Counter란?
- `Counter`는 파이썬의 기본 자료구조인 **딕셔너리(Dictionary)**를 확장해서 만든 특수한 클래스로, 리스트나 문자열 같은 데이터를 넣으면, **데이터의 요소들을 키(Key)로, 그 요소가 등장한 횟수를 값(Value)으로 갖는 딕셔너리 형태로 만들어 준다.**
``` python
from collections import Counter

my_list = ['a', 'b', 'a', 'c', 'b', 'a']
print(Counter(my_list))
# 출력: Counter({'a': 3, 'b': 2, 'c': 1})

print(Counter("hello"))
# 출력: Counter({'l': 2, 'h': 1, 'e': 1, 'o;: 1})
```
# 2. Counter의 장점: 에러가 나지 않는다
- 일반적인 딕셔너리에서는 존재하지 않는 키를 찾으려고 하면 `KeyError`라는 에러가 발생하면서 프로그램이 멈추는데, `Counter`는 존재하지 않는 데이터를 찾으려고 하면 에러 대신 숫자 `0`을 반환한다.

``` python
from collections import Counter

c = Counter(['apple', 'banana'])

print(c['apple'])   # 출력: 1
print(c['grape'])   # 출력: 0 (에러가 발생하지 않음)
```

# 3. 알아두면 무조건 쓰이는 Counter의 핵심 매서드
1. **`most_common(n)`: 가장 많이 나온 데이터 찾기** <br/>
가장 등장 빈도수가 높은 데이터부터 순서대로 보여준다. 괄호 안에 숫자 $n$을 넣으면 상위 $n$개까지만 뽑아줍니다.

``` python
from collections import Coutner

c = Counter(['a', 'a', 'a', 'b', 'b', 'c'])

print(c.most_common(2))
# 출력: [('a', 3), ('b', 2)] (리스트 안에 튜플 형태로 반환)
```

2. **`elements()`: 개수만큼 다시 풀어서 보여주기** <br/>
카운트된 숫자만큼 해당 요소들을 다시 반복해서 반환한다.

``` python
from collections import Counter

c = Counter({'a': 2, 'b': 3})

print(list(c.elements()))
# 출력: ['a', 'a', 'b', 'b', 'b']
```

3. **집합 연산 (덧셈, 뺄셈, 교집합, 합집합)** <br/>
`Counter` 객체끼리는 덧셈(+)이나 뺄셈(-) 같은 연산이 가능하다. 이 기능은 두 데이터 집합을 비교할 때 매우 유용하다. 

``` python
from collections import Counter

c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])

print(c1 - c2)
# 출력: Counter({'a': 1, 'c': 1})

print(c1 + c2)
# 출력: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
```