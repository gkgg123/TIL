import sys
sys.stdin=open('GNS_test_input.txt','r')

di_pla={
    'ZRO':0,
    'ONE':1,
    'TWO':2,
    'THR':3,
    'FOR':4,
    'FIV':5,
    'SIX':6,
    'SVN':7,
    'EGT':8,
    'NIN':9
}

Li_pla=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", 
"SIX", "SVN", "EGT", "NIN"]


T=int(input())

for tc in range(1,T+1):
    TTC=input().split()
    pla_input=list(input().split())
    result=[]
    print(TTC)

    for j in pla_input:
        result.append(di_pla[j])
    temp=sorted(result)
    print('#{}'.format(tc))

    total=''
    for k in temp:
        total+=Li_pla[k]+' '
    print(total)