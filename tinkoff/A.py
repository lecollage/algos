def calc(n: int, s: str = ""):
    if not n:
        print(s)
        return

    calc(n-1, s+"1")    
    calc(n-1, s+"0")



n = int(input())
calc(n, "") 


# calc(1) -> ['0', '1']
# calc(2) -> ['00', '01', '10', '11']