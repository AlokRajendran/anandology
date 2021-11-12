# Problem 15: Reimplement the unique function implemented in the earlier examples using sets.

def unique(li):
     
    li2 = []
    li_set = set(li)
  
    unique_li = (list(li_set))
    for i in unique_li:
        li2.append(i) 
    return li2
 

li = [1, 2, 1, 3, 2, 5]
print(unique(li))