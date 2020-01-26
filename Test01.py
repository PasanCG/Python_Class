def babysmile(a_smile,b_smile):
    if a_smile==True and b_smile==True:
        return True
    elif a_smile==False and b_smile==False:
        return True
    else:
        return False

def int_sum(a,b):
    if a==b:
        return (a+b)*2
    else:
        return (a+b)

def time_machine (time):
    hour_arr=[]

    for i in range (time+1,24,1):
        hour_arr.append(i)
    return hour_arr

def hours_1(h):
    return list(range(h+1,24))

def parameter(e,f,neg):
    if neg:
        return (e<0) and (f<0)
    else:
        return (e>0 and f<0) or (e<0 and f>0)

def font_back(s):
    if len (s) ==1:
        return s
    else:
        mid = s[1:-1]
        f = s[0]
        l = s[-1]

        return (l+mid+f)

def repeat(p,q=3,r=3):
    if len(p)>=q:
        first = p[0:q]
        last= p[-q]
        return(str(first)*r + str(last)*r)
    else:
        return("no of charactrs should be long")


def last_ch(p, q=3, r=3):
    if len(p) >= q:
        first = p[-q:]
        return (str(first) * r)
    else:
        return ("no of charactrs should be long")

def newlist(list):
    new_list=[]
    g_list_len = len(list)
    new_list_len = g_list_len*2
    last_el = list[-1]
    for new_el in range(new_list_len):
        new_list.append(0)
        new_list[-1] = last_el
    return new_list

def zero_list_2(g_1):
    new_list= []
    for i in range(len(g_1)*2):
        if i == (len(g_1)*2-1):
            new_list.append(g_1[-1])
        else:
            new_list.append(0)
    return new_list

def zero_list_3 (g_1):
    new_list = [0]*len(g_1)*2
    new_list[-1] = g_1[-1]
    return new_list

def list_count_9(g_list):
    count =0

    for i in g_list:
         if i == 9:
            count = 1+ count
         else:
            count = 0+ count
    return count

def list_count_9_nw(g_list):
    return g_list.count(9)






if __name__ == '__main__':

    # val =babysmile(True, False)
    # print(val)

    # val1 = babysmile(False,False)
    # print(val1)

    # problem 3
    # val3 = int_sum(9,10)
    # print(val3)

    #problem 4
    # val4 = time_machine(12)
    # print(val4)

    # problem 4 method 2
    # val4_1 = hours_1(10)
    # print(val4_1)

    # problem 5
    # val5 = parameter(12,-14,True)
    # print(val5)

    # problem 6
    #val6 = font_back("Pasan")
    #print(val6)


    # problem 7
    # val7 = repeat("Pasan",4,8)
    # print(val7)

    # problem 8
    # val8 = last_ch("Pasan",2,1)
    # print(val8)

    # problem 9
    #  val9 = zero_list_2([1,2,3])
    #  print(val9)
    #  print(list_count_9([1,2,9,9,19]))
    print(list_count_9_nw([1,2,3,9,9,9]))

    f=lambda a:a*a
    print(f(2))
    h= lambda x,y: x*x+y
    print(h(3,1))