test_list = [6,1]
print("The original list : " + str(test_list))
K = 2
K2 = 4

res = []
for i in test_list:
    for ele in range(K):
        res.append(i)
         
print("The list after adding elements : " + str(res))

