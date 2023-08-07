weight = int(input('Weight: '))
kgOrLb = input('(K)g or (L)bs: ').lower()

if kgOrLb == 'l':
  print('Weight in KG: ', weight * 0.45359237)
else:
  print('Weight in LB: ', weight * 2.205)

