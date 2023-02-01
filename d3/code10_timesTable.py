# 구구단
_ = '_'
__ = '-'
print(f'{_*15}')
print('▶구구단을 외자◀')
print(f'{__*15}')
for x in range(2,10):
    print('\n_S2_['+str(x)+'단]_S2_\n')
    for y in range(2,10):
        print(f'{x} X {y} = {x*y:>2}', end= ' | ')      # :>2 정렬맞추기
    print()         # 단 구분