def calc(n: int, s: str = ""):
    if not n:
        print(s)
        return 

    calc(n-1, s+"1")    
    calc(n-1, s+"0")



n = int(input())
calc(n, "")