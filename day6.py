my_list=[2,7,11,15]
target=9
for num in my_list:
    compliment=target-num
    if compliment in my_list:
        print(f"pair found:({num},{compliment})")
        break

