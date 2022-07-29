# Programmers
프로그래머스 코딩 연습

## C++
push_back() = 담기

erase() = 지우기

min_element() = 최솟값 찾기

empty() = 빈문자열 찾기

sort(arr.begin(), arr.end()); = 오름차순 정렬

isdigit() = 숫자확인

unique() = 중복제거

sort(arr.begin(), arr.end()) = 오름차순

sort(arr.begin(), arr.end(), greater()) = 내림차순

to_string(n) = n을 문자열로 전환

reverse() = 거꾸로 뒤집기

min() = min값 찾기

max() = max값 찾기

sqrt(n) = n의 제곱근

---
## **string 클래스의 특징**

- 특징 1 : 문자의 끝에 null문자(‘\0’) 등이 포함되지 않는다.
- 특징 2 : 마치 배열처럼 한 문자씩 다룰 수 있다.
- 특징 3 : string 클래스 끼리는 문자열을 합치는 것이 **+ 연산자 하나만으로** 가능하다.
- 특징 4 : 문자열을 사전순으로 정렬할 때도 string 변수를 사용하면 편리하다.
- 이 외에 다양하게 쓸 수 있는 멤버함수들이 존재힌다.

## **string 의 인덱스 접근**

- 배열처럼 접근하기
    - string str = “TEST”; 일 때, str[0] 은 ‘T’를 반환. 이 때 반환되는 문자는 char 형
- .at(index)로 접근하기
    - string str = “TEST”; 일 때, str.at(1) 은 ‘E’를 반환. 이 때 반환되는 문자는 char 형

---

## **문자열의 맨 앞과 맨 끝 문자 반환**

- str.front(); -> 맨 앞 문자 반환
- str.back(); -> 맨 끝 문자 반환

---

## **문자열의 길이 반환**

- **str.size(); 혹은 str.length(); 둘 다 사용 가능.**

---

## **숫자를 문자열(string)로, 문자열을 숫자로 바꾸기**

- **숫자->문자열 전환 :** **to_string(숫자);** 로 사용할 수 있다.
```cpp
int a = 7;
string str1;
str1 = to_string(a); // 7이 string "7"로 변환되어 str1에 저장된다.
```
- **문자열->숫자 전환** : int 타입, double 타입 등 숫자의 타입에 따라 아래와 같이 사용합니다. (stoi 함수)
```cpp
string str_a ="7";
string str_b ="7.02";
string str_c ="3.14";
string str_d = "2300000000";

int after_a = stoi(str_a); // "7"을 int형 7로 바꿔줌
double after_b = stod(str_b); // "7.02"를 double형 7.02로 바꿔줌
float after_c = stof(str_c); // "3.14"를 float형 3.14로 바꿔줌
long int after_d = stof(str_d); // "2300000000"을 long int형으로 바꿔줌
```
## **string 의 유용한 함수들**

### **str.empty();**
문자열이 비었나 확인한다. 이것은 문자열의 size 혹은 length 값이 0인지 아닌지를 보는 것.

### **swap(str1,str2)**
str1, str2 문자열을 서로 swap 한다. (바꾸기)

### **str.clear();**
str에 들어있던 문자열을 삭제한다. (단, capacity 값은 그대로 유지)

### **str1.append(str2);**
str 문자열 맨 뒤에 str2 문자열을 추가한다.
```cpp
  string str1 = "test";
  string str2 = "yo";
  str1.append(str2); // "testyo" 반환
  str2.append("tete"); // "yotete" 반환
  // 팁 : str1+str2 를 하면 str1에 append(str2)를 한 효과와 동일하다.
  ```
  
  ### **str.find(str2);**
str에서 문자열 str2를 찾고, 이것의 str에서의 시작점 인덱스를 반환한다.
```cpp
 string str1 = "TEST";
  string str2 = "ST";
  str1.find(str2); // 2 반환 (TEST에서 ST의 S는 2번째 인덱스므로)
  ```
  
  ### **str.substr();**
문자열의 일부분을 반환한다. -> **반환형이 string임**
```cpp
  string str = "TESTtest";
  str.substr(3); // 3번째 인덱스인 T부터 끝까지 반환 -> Ttest 반환
  str.substr(3, 2); // 3번째 인덱스인 T부터 2 길이만큼의 문자열 반환
  // 즉, Tt 가 반환된다.
  ```
  
  **문자열의 사전 순서 비교 - 부등호로 비교 가능(<,>,==)**
  ```cpp
    string str1 = "aaad";
  string str2 = "aaaf";
  cout << (str1 < str2); // 1(참)이 반환된다.
  // 즉, str1과 str2 중 사전 순으로 str1이 더 앞선 글자므로, str2보다 작다.
  ```
  
**+ 연산자로 두 문자열을 쉽게 합칠 수 있다.**
```cpp
  string str1 = "10";
  string str2 = "6";

  cout << (str1 < str2); // 1이 반환된다.
  // 즉, 사전순으로는 10이 6보다 앞서 있기 때문에.

  string str3 = str1 + str2; // "106"
  string str4 = str2 + str1; // "610"

  cout << (str3 < str4); // "610"이 사전 순서상 더 뒤이므로 크고, 1이 반환된다.
  // 이를 응용하면, 같은 자릿수로 받아진 정수 형태(ex: "1234")의 문자열 비교는
  // 단순히 int형끼리 비교하는 것과 같다.
```
  
