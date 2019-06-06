def sum_of_numbers(list_of_num,filter_func=None):
    sum1=0
    if(filter_func!=None):
        for i in filter_func(list_of_num):
            sum1+=i
        return sum1
    else:
        for i in list_of_num:
            sum1+=i
        return sum1

        #Remove pass and write the logic here

def even(data):
    m=[]
    for k in data:
        if(k%2==0):
            m.append(k)
    return m

    #Remove pass and write the logic here

def odd(data):
    l=[]
    for j in data:
        if(j%2!=0):
            l.append(j)
    return l

        #Remove pass and write the logic here

sample_data = range(1,11)

print(sum_of_numbers(sample_data,"Odd"))
