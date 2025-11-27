buyers = [['张三', 288], ['李四', 588],
          ['王五', 688], ['刘六', 1288],
          ['杨七', 1688]]

gold_buyer = []
vip_buyer = []

while buyers:
    index_buyer = buyers.pop()    # 弹出, 默认从尾部弹出
    # print(index_buyer)
    if index_buyer[1] >= 1000:
        # vip 买家
        vip_buyer.append(index_buyer)
    else:
        # gold 买家
        gold_buyer.append(index_buyer)
print(f'{vip_buyer=}')
print(f'{gold_buyer=}')
print(f'{buyers=}')