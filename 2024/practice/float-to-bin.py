dec = float(input("Input Decimal; "))

def FloatToBin(_float):
  res = ''
  for i in range(-32, 33):
      if _float - 2**-i >= 0:
          res += '1'
          _float -= 2**-i
      elif '1' in res:
          res += '0'
      if i == 0:
          res += '.'
      if _float == 0:
          break
        
print (FloatToBin(dec))
