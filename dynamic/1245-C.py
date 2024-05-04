def calc(s: str):
    if 'w' in s or 'm' in s:
        return 0
    N = 10 ** 9 + 7
    dp = [0 for _ in range(0, len(s)+1)]

    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s)+1):
        if s[i-1] == s[i-2] and s[i-1] in "nu":
            dp[i] = (dp[i-1] + dp[i-2]) % N
        else: 
            dp[i] = dp[i-1]

    return dp[-1]


s = input()
print(calc(s))



'''
ouuokarinn
если произнести 'w', то будет записано «uu» вместо «w», и если произнести 'm', то будет записано «nn» вместо «m»

ouuokarinn
owokarinn
owokarim


uuuu
1,2 wuu
2,3 uwu
3,4 uuw
1,2 and 3,4
as is uuuu



1
1
2
3
5
8
13


10000


        | 
xxuuuxxnnn

xxuuuxx   -> 3
xxuuuxxn  -> 3
xxuuuxxnn -> ?

xxx...xxx -> a
xxx.....xnn..n -> a
xxx.....xnn..nn -> b = a + a    | a*2
xxx.....xnn..nnn -> c = a + b


dp[-1]%(10^9+7)

|x|

(a + b + ... + x + y + z) % n

((a + b) % n + c) % n

((a % n) + (b % n) + ... + (z % n)) % n

(a + b) % n == (a % n + b % n) % n

(a + b + c) % n = ((a + b) + c) % n = ((a +b ) % n + c % n ) % n
5 7
2 + 1 = 3 = 0



xxuuuxxn
xxuuuxxm
xxuuuxxnn

nn, m
nnn, 

2
3

0 1 2 3 4 5 6 7 8 9 10
1 1 1 2 3 3 3 3 3 6 9

2
    




  |
xxuu




xxuuu



1*2*1*3

'''




