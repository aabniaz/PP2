def chicken_rabbit(numheads, numlegs):
    rabbit_legs = numlegs - 2 * numheads
    rabbit_heads = rabbit_legs / 2
    chicken_heads = numheads - rabbit_heads
    print(int(chicken_heads), int(rabbit_heads), end="")

chicken_rabbit(35, 94)
