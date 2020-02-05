T=int(input())

for tc in range(1,T+1):
    st=input()
    if len(st)==1:
        print('..#..')
        print('.#.#.')
        print('#.{}.#'.format(st))
        print('.#.#.')
        print('..#..')
    else:
        print('..',end='')
        for i in range(len(st)):
            if i != len(st)-1:
                print('#...',end='')
            else:
                print('#..')
        
        for i in range(len(st)):
            print('.#.#',end='')
        print('.')

        for i in range(len(st)):
            print('#.{}.'.format(st[i]),end='')
        print('#')

        for i in range(len(st)):
            print('.#.#',end='')
        print('.')

        print('..',end='')
        for i in range(len(st)):
            if i != len(st)-1:
                print('#...',end='')
            else:
                print('#..')

