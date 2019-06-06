principal_amount=4000
duration=12
rate_of_interest=13

simple_interest =lambda principal_amount,duration,rate_of_interest:(principal_amount*duration*rate_of_interest)/100#Write the lambda expression here

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    print("platinum member")
else:
    print("gold member")
