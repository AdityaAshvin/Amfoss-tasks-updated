number = []; t = 0;i = 999;

def palindrome(n):
  string_n = str(n)
  reverse_n = string_n[::-1]
  if reverse_n == string_n:
    number.append(n)
  return number

while(i > 99):
  for j in range(100,999):
    palindrome(i*j)
  i = i-1

print(max(number)) 
