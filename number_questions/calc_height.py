# 12)Lily found an old wooden ladder in her grandfather’s attic. It looked normal, but when she tried to climb it, she noticed something strange—the steps weren’t evenly spaced!
# The first step was 4 cm high.
# The second step was 8 cm high.
# The third step was 7 cm high.
# The fourth step was 11 cm high.
# She realized that:
# •	Every odd step (1st, 3rd, 5th, …) followed a pattern starting from 4 and increased by 3 each time.
# •	Every even step (2nd, 4th, 6th, …) followed a pattern starting from 8 and also increased by 3 each time.
# Lily wanted to count how high the first N steps would be before she climbed further. Can you help her write a Python program to find out?


def calcHeight(n):
    height=0
    odd_step=4
    even_step=8
    for i in range(1,n+1):
        if i%2!=0:
            height+=odd_step
            odd_step+=3
        else:
            height+=even_step
            even_step+=3
    return height


ans=calcHeight(10)
print(ans)
