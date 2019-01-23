# -*- coding: utf-8 -*-
"""
CSS 221
M1LAB
Ashley Register
Jan 23, 2019
"""
def main():
    """Bottles of beer song"""
    # 1 see a var
    bottles = 99
    while bottles >= 0:
        print(bottles, "bottles of beer")
        bottles = bottles - 1
    # 2 see a for loops
    """for beer in range(99, -1, -1):
        print(beer, "beers")"""
        
    #range(start,stop,step)
    #0 based by defalt 
    # start <= i < stop

if __name__ == "__main__":
    main()        

