def linear_search_product(productlist,target_product):
    indices=[]
    for n in  range(len(productlist)):
        if productlist[n]== target_product:
            indices.append(n)
    return indices


products=["watch","boot","sandal","watch","shoes","watch","ring"]
target="watch"
target2="apple"
result=linear_search_product(products,target)
print(result)
