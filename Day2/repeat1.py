def main():
    number = get_number()
    yeah(3)


def get_number():
    while True:
        n = int(input( "What's n ?" ))
        if n > 0:
            break
        return n

def yeah(n):
    for _ in range(n):
        print("yeah")

main()    
    