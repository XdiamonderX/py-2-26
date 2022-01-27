import random
num = random.randint(1,20)
ans = input("Give me a number from 1 ~20:")
ans = int(ans)
g = 10
if ans == num:
    print("You are correct!")
    g = 0
elif ans < num:
    ans2 = input("Too small!:")
    c = 0
    while c < 3:
        ans2 = int(ans2)
        if ans2 == num:
            print("You are correct!")
            g = 0
            break
        elif ans2 < num:
            ans2 = input("Too small!:")
            c = c + 1
        elif ans2 > num:
            ans2 = input("Too big!:")
            c = c + 1
    print("The answer is",num,"!")
elif ans > num:
    ans2 = input("Too big!:")
    c = 0
    while c < 3:
        ans2 = int(ans2)
        if ans2 == num:
            print("You are correct!")
            g = 0
            break
        elif ans2 < num:
            ans2 = input("Too small!:")
            c = c + 1
        elif ans2 > num:
            ans2 = input("Too big!:")
            c = c + 1
    print("The answer is",num,"!")



























































