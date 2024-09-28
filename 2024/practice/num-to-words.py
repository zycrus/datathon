ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


num = int(input("Enter Number: "))
res = ""

def threeDigitsToWords(digits):
    res = ""
    _num = digits
    while(_num > 0):
        if _num > 99:
            res += str(ones[_num//100]) + ' hundred '
            _num -= _num//100*100
        elif _num > 19:
            res += str(tens[_num//10]) + '-'
            _num -= (_num//10)*10
        elif num > 0:
            res += str(ones[_num])
            _num -= _num
    return res

def NumToWords(_num):
  if _num == 0:
    return "zero"
  if _num >= 1000000000:
      res += threeDigitsToWords(num//1000000000).rstrip("-") + " billion "
      _num -= (_num//1000000000)*1000000000
  if _num >= 1000000:
      res += threeDigitsToWords(num//1000000).rstrip("-") + " million "
      _num -= (_num//1000000)*1000000
  if _num >= 1000:
      res += threeDigitsToWords(num//1000).rstrip("-") + " thousand "
      _num -= (_num//1000)*1000
  res += threeDigitsToWords(_num)
  return res
    
    
print(NumToWords(num))
