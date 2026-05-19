num_1=float(input('enter num_1 : '))

choice=input ('enter your choice +,_,*,/,**, %:')


num_2=float(input('enter num_2 : '))


 
if choice == '+':
    print('sum  : ',num_1 + num_2)

elif choice == '-':
    print('sub :', num_1 - num_2) 
    
elif choice == '*':
    print('mul :', num_1 * num_2 )
    
elif choice == '/':
    print('divide:',num_1 / num_2)
 
elif choice == '**':
    print('exponent:',num_1**num_2)

elif choice == '%':
    print('remainder :', num_1 % num_2)
             
else :
    print('invalid opearator')