
def add(num):

    if num >= 9:
        return num + 1
    
    total_num = num + 1
    print(total_num)
    return add(total_num)

m_num = add(0)
print(m_num)