def sum_all(function, data):
    sum1=0
    for i in list_of_nos:
        if (function(i)):
            sum1=sum1+i
        
    return sum1

list_of_nos=[100,200,300,500,1040]

greater = lambda i:i>10
   # sum_all(greater,i)#Write the lambda expression for question1

divide = lambda i:((i%10==0) and (i<=100))
    #sum_all(divide,i)#Write the lambda expression for question2

range_of_values = lambda i:(25<=i<=50)
    #sum_all(range_of_values,i)#Write the lambda expression for question3


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
