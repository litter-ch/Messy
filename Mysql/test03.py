with open('acount.txt',mode='r',encoding='utf-8') as f:
    for lin in f:
        line = lin.strip()
        if not line:
            continue
        data_list = line.split(',')
        print(data_list)

