## Zajęcia 1 16.10.2023

### Informacje na temat przedmiotu

Prowadzący: mgr inż. Bartosz Fijałkowski
mail: bf55466@st.amu.edu.pl

Gdyby była potrzeba przedyskutowania czegoś to możemy zostać po zajęciach. Można też kontaktować się ze mną mailowo.

W celu zaliczenia przedmiotu należy zdobyć punkty za zadania na laboratoriach oraz zaliczyć kolokwium.
Punktowane zadania będziemy wykonywać na laboratoriach oraz po nich (przed następnymi zajęciami), ich ilość determinuje ocenę.
Oprócz tego należy zaliczyć kolokwium z wyrażeń regularnych na ostatnich zajęciach. Sam wynik kolokwium 
nie będzie wpływał na ocenę, ale bez zdanego kolowkium nie da się zaliczyć przedmiotu. Punktacja za zadania jest następująca:
  - mniej niż 30 punktów - 2
  - 30-34- 3
  - 35-39- 3.5
  - 40-44- 4
  - 45-49- 4.5
  - więcej niż 49- 5

#### Wysyłanie zadań 

Proszę stworzyć prywatne repozytorium na https://git.wmi.amu.edu.pl/ o nazwie djfz-2023-sNRINDEKSU oraz dać 
prawa do odczytu użytkownikowi bfijalkowski (prowadzący przedmiot). W NRINDEKSU proszę wpisać swój nr indeksu, np. djfz-2023-s123456.

Następnie w swoim repozytorium proszę zforkować niniejsze repozytorium: `git pull git@git.wmi.amu.edu.pl:bfijalkowski/DJFZ-2023.git`
W ten sposób będziemy aktualizować zadania co zajęcia.

Proszę rozwiązać zadanie TASKX02 lub TASKX03 w zależności od numeru indeksu. W tym celu należy dodać plik `run.py`
w odpowiednim katalogu. Za pomocą `run_reports.py` można sprawdzić ilość punktów.

Do repo proszę dodawać wyłącznie plik `run.py` w odpowiednim katalogu, chyba że w zadaniu jest zaznaczone inaczej.
Proszę również nie modyfikować innych plików.

Wszystkie zadania należy robić w terminie zaznaczonym w `description.txt`. Po terminie będę podawał punktację za pomocą USOSa w "sprawdziany".

Zadania robimy do dnia poprzedzającego następne zajęcia.

#### Aktualizacja repozytorium

We własnym repozytorium:

`git pull git@git.wmi.amu.edu.pl:bfijalkowski/DJFZ-2023.git`

## Zajęcia 1 16.10.2023 Automaty deterministyczne skończone

B00 - zadanie wykonywane wspólnie na zajęciach
B01-B04, B06-B09 - po jedno dla każdego
B05 - jedno dla wszystkich

## Zajęcia 2 30.10.2023 Automaty niedeterministyczne skończone

C00 - zadanie wykonywane wspólnie na zajęciach
C01-C03, C04-C06 - po jedno dla każdego

## Zajęcia 3 13.11.2023 Wyrażenia regularne

D01 - D04 - do wykonania przez każdego

Dokumentacja wyrażeń regularnych w python3: https://docs.python.org/3/library/re.html

### Podstawowe funkcje

search - zwraca pierwsze dopasowanie w napisie

findall - zwraca listę wszystkich dopasowań (nienakładających się na siebie)

match - zwraca dopasowanie od początku string

To tylko podstawowe funkcje, z których będziemy korzystać. W dokumentacji opisane są wszystkie.

### Obiekt match

```
import re
answer = re.search('na','banan')
print(answer)
print(type(answer))
print(answer.start())
print(answer.end())
print(answer.group())

answer = re.search('na','kabanos')
print(answer)

if answer:
    print(answer.group())
else:
    pass
```

### Metaznaki


- [] -  zbiór znaków
- . - jakikolwiek znak

- ^ - początek napisu
- $ - koniec napisu

- ? - znak występuje lub nie występuje
- \* - zero albo więcej pojawień się
- \+ - jeden albo więcej pojawień się
- {} - dokładnie tyle pojawień się

- | - lub
- () - grupa
- \ -znak ucieczki

- \d digit
- \D nie digit
- \s whitespace
- \S niewhitespace


### Flagi

Można użyć specjalnych flag, np:
`re.search('ma', 'AlA Ma KoTa', re.IGNORECASE)`.

### Przykłady (objaśnienia na laboratoriach)

```
import re

text = 'Ala ma kota i hamak, oraz 150 bananów.'

re.search('ma',text)
re.match('ma',text)
re.match('Ala ma',text)
re.findall('ma',text)

re.findall('[mn]a',text)
re.findall('[0-9]',text)
re.findall('[0-9abc]',text)
re.findall('[a-z][a-z]ma[a-z]',text)
re.findall('[a-zA-Z][a-zA-Z]ma[a-zA-z0-9]',text)
re.findall('\d',text)

re.search('[0-9][0-9][0-9]',text)
re.search('[\d][\d][\d]',text)

re.search('\d{2}',text)
re.search('\d{3}',text)

re.search('\d+',text)

re.search('\d+ bananów',text)
re.search('\d* bananów','Ala ma dużo bananów')
re.search('\d* bananów',text)
re.search('ma \d? bananów','Ala ma 5 bananów')
re.search('ma ?\d? bananów','Ala ma bananów')
re.search('ma( \d)? bananów','Ala ma bananów') 

re.search('\d+ bananów','Ala ma 10 bananów albo 20 bananów')
re.search('\d+ bananów$','Ala ma 10 bananów albo 20 bananów')

text = 'Ala ma kota i hamak, oraz 150	bananów.'

re.search('\d+ bananów',text)

re.search('\d+\sbananów',text)

re.search('kota . hamak',text)

re.search('kota . hamak','Ala ma kota z hamakiem')

re.search('kota .* hamak','Ala ma kota lub hamak')

re.search('\.',text)

re.search('kota|psa','Ala ma kota lub hamak')

re.findall('kota|psa','Ala ma kota lub psa')

re.search('kota (i|lub) psa','Ala ma kota lub psa')

re.search('mam (kota).*(kota|psa)','Ja mam kota. Ala ma psa.').group(0)

re.search('mam (kota).*(kota|psa)','Ja mam kota. Ala ma psa.').group(1)

re.search('mam (kota).*(kota|psa)','Ja mam kota. Ala ma psa.').group(2)
```

### Przykłady wyrażenia regularne 2 (objaśnienia na laboratoriach)

####  ^
```
re.search('[0-9]+', '123-456-789')
re.search('[^0-9][0-9]+[^0-9]', '123-456-789')
```

#### cudzysłów
'' oraz "" - oznaczają to samo w pythonie

' ala ma psa o imieniu "Burek"'

" ala ma psa o imieniu 'Burek' "

' ala ma psa o imieniu \'Burek\' '

" ala ma psa o imieniu \"Burek\" "

#### multiline string

#### raw string

przy raw string znaki \ traktowane są jako zwykłe znaki \

chociaż nawet w raw string nadal są escapowane (ale wtedy \ pozostają również w stringu bez zmian)

https://docs.python.org/3/reference/lexical_analysis.html

dobra praktyka - wszędzie escapować

```
'\\'
print('\\')

r'\\'
print(r'\\')


print("abcd")
print("ab\cd")
print(r"ab\cd")

print("ab\nd")
print(r"ab\nd")


print("\"")
print(r"\"")

print("\")
print(r"\")

re.search('\\', r'a\bc')
re.search(r'\\', r'a\bc')
re.search('\\\\', r'a\bc')
```