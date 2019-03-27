#!/usr/bin/env python3

def bigger_price(limit: int, data: list) -> list:
    output = {}
    count = 0
    for index in data:
        for key, value in index.items():
            output[key] = value
            #output.update({key:value})
            #print(key)
    #print(output)
    #sort_by_value = sorted(index.items(), key=lambda kv:kv[1])
    #print(sort_by_value)
        #for key,value in index.items():
            #if count < limit+1:
                #output.update({key:value})
                #output[key]=value
                #print(key)
                #print(value)
                #count = count+1
    #return list(output)
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]

if __name__ == '__main__':
    print(bigger_price(2,[
        {"name": "bread", "price": 100},
        {"name": "wine", "price":183},
        {"name": "meat", "price":15},
        {"name": "water", "price":1}
        ]))
