# 閏年判斷規則：
# 1. 西元年份能被400整除，為閏年
# 2. 西元年份能被4整除但不能被100整除，為閏年
# 3. 其他皆為平年

# 判斷是否為閏年
def isLeapYear(input_year):
  input_year = int(input_year)
  if (input_year % 400 == 0) or (input_year % 4 == 0 and input_year % 100 != 0):
    print("a leap year")
  else:
    print("a normal year")
      
if __name__ == '__main__':
  try:
    while True:
      input_year = input('請輸入西元年：')
      if input_year == '':
        break
      isLeapYear(input_year)
  except EOFError:
    pass