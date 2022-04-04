"""
Given a number n as input, write it In words. Note that n is between 0 and 999.
Input-> 140
Output-> one hundred forty
"""


num = int(input("Enter Number: "))
output = ""

once = [' ','One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ',
        'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
        'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']

tens = ['','','Twenty ', 'Thirty ', 'Forty ', 'Fifty ',
        'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']

hun = ['','One hundred','Two hundred','Three hundred','Four hundred','Five       hundred','Six hundred','Seven hundred','Eight hundred','Nine hundred']

if (num==0):
  output = "Zero"
  
elif (num<=19):
  output = once[num]

elif (num<=99):
  output = tens[num//10]+""+once[num%10]

elif (num<=999):
  output = hun[num//100]+""+tens[num//10]+""+once[num%10]

else:
  print("Enter number between 0 to 999")

print(output)