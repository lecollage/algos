/*
У Пети есть слово t, он хочет, чтобы из него получилось слово p. Петя начинает вычеркивать буквы в некотором порядке, который задан перестановкой номеров букв слова t:
a1…a|t|. Заметим, что после вычеркивания буквы нумерация не меняется.

Его брат Вася боится, что Петя может удалить слишком много букв, и слово p не получится.
Задача Васи состоит в том, чтобы в некоторый момент времени остановить брата и закончить вычеркивание самому, получив после этого слово p.
Так как Пете нравится это занятие, Вася хочет остановить его как можно позже.
Ваша задача — сообщить, сколько букв может вычеркнуть Петя до того, как его остановит Вася.

Гарантируется, что слово p можно получить вычеркиванием букв из t.

Входные данные
Первая и вторая строки входного файла содержат слова t и p, соответственно. Слова состоят из строчных букв латинского алфавита (1≤|p|<|t|≤200000).

Следующая строка содержит перестановку a1…a|t| номеров букв, задающую порядок, в котором Петя вычеркивает буквы слова t (1≤ai≤|t|, все ai различны).

Выходные данные
Выведите одно число — максимальное число букв, которые может вычеркнуть Петя.

входные данные
ababcba
abb
5 3 4 1 7 6 2

выходные данные
3

a 1
b 2
a 3
b 4
c 5
b 6
a 7

a 1
b 2
a 3
b 4
b 6
a 7

a 1
b 2
b 4
b 6
a 7

a 1
b 2
b 6
a 7

b 2
b 6
a 7

l     m     r
5 3 4 1 7 6 2

a 1
b 2
b 6
a 7

| | |
a b b a
| | |
a b b

      l m   r
5 3 4 1 7 6 2

| |   |
a b a b c b a
| |
a b b
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var in = bufio.NewReader(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func readInput() (string, string, []int) {
	var t, p string

	fmt.Fscan(in, &t)
	fmt.Fscan(in, &p)

	array := make([]int, 0)

	for i := 0; i < len(t); i++ {
		var elem int
		fmt.Fscan(in, &elem)

		array = append(array, elem)
	}

	return t, p, array
}

// check if symbols from str1 are included in the same order to str2
func doesInclude(str1, str2 string) bool {
	symbols1 := strings.Split(str1, "")
	symbols2 := strings.Split(str2, "")

	var i = 0
	for _, symbol1 := range symbols1 {

	sym2:
		for ; i < len(symbols2); i++ {
			if symbols2[i] == symbol1 {
				break sym2
			}
		}
	}

	return true
}

func calculate(t, p string, array []int) int {

	return 0
}

func main() {
	// fmt.Println("START >> ")
	t, p, array := readInput()

	fmt.Println("1 >> ", t, p, array)

	result := calculate(t, p, array)

	fmt.Println(result)

	defer out.Flush()
}
