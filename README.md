# Калькулятор полиритмов
 Простой калькулятор полиритмов написанный на Python с использованием GPT4

> [!NOTE]
> Считает в ударах в минуту (BPM) и в герцах (Hz) _(может считать отрицательные числа)_
> Вывод сразу нескольких ритмов (2, 3, 4...) _(не поддерживает плавающую запятую/отрицательные значения)_
> Отсчет от определенного ритма (240гц на 4ом, на 6ом будет 360, т.к. 1й равен 60)
> Поддерживает плавающую запятую в герцах и ударах в минуту (120.5, 60.8...) _(автоматически сокращается до десятков)_

> [!IMPORTANT]
> Для работы необходим Python _(по сути любой версии?)_

## Как это работает?

У вас есть ритм, условные 60 ударов в минуту\
Вам необходимо получить сколько ударов в минуту будет если между основным ударом, будем второстепенный\
Вы выбираете первое действие, вводите количество ударов в минуту, и вводите количество ударов между\
На выходе вы получаете 120 ударов в минуту\

Есть частота в 240 герц\
Вы знаете что это число происходит от 4х периодов основной частоты, но вам необходимо узнать сколько будет 6 периодов\
Вы выбираете четвертое действие, вводите количество герц, вводите сколько это периодов, и вводите сколько вам нужно периодов\
На выходе вы получаете 360 герц\

### Зачем так сложно?
_Мне необходимо было посчитать много таких значений, и делать это в голове а уж тем более с плавающей запятой, как то долго.\
И ладно бы если это были бы только простые типа, 60*2=120 и др., но мне так же необходимо было вычислять не от начала.\
А если неправильно посчитать, например, если основная частота не 60, а 240, то 6ой ритм будет не 360, а 1440.\
Да я могу условно посчитать 240*1.5=360, но это уже плавающая запятая._

Не бейте тапками, это простой скрипт сделанный за 5 минут на коленке в ChatGPT, может он и вам пригодится когда нибудь, а я просто поделился им потому что мне не сложно.
