## Распределение студентов по билетам.

При распределении было принято решение использовать криптографическую функцию keccak, используемую для хеширования сигнатур функций в solidity.

Пример работы программы:

```console
>> python main.py --file students.txt --numbilets 20 --parameter 42
Иванов Иван Иванович: 3
Ярцев Ярослав Ярославович: 1
Петров Петр Петрович: 20
Владимиров Владимир Владимирович: 10
Сергеев Сергей Сергеевич: 7
Николаев Николай Николаевич: 6
Романов Роман Романович: 17
Максимов Максим Максимович: 8
Фитисов Артем Вячеславович: 19
```
