#!/usr/bin/env python
# coding: utf-8

# In[69]:


from tabulate import tabulate
import statistics
import numpy as np
lst = {'Nama':[],'Nilai':[],'Keterangan':[]}
str = ""
sums = 0
counts = 0
n = int(input("Masukkan banyak data : "))


for i in range(0, n):
    print("\n")
    ele = [input("Masukkan nama      :"), int(input("Masukkan nilai     :")),""]
    if ele[1]>= 70:
                ele[2] = "LULUS" 
    if ele[1] < 70:
                ele[2] = "GAGAL"
           
    lst["Nama"].append(ele[0])
    lst["Nilai"].append(ele[1])
    lst["Keterangan"].append(ele[2])
print("\n")
print(tabulate(lst,headers='keys',tablefmt='fancy_grid'))
print("\n")


lsls = [row[2] for row in lst]
print("Rata-rata nilai    :",statistics.mean(lst["Nilai"]))
print("Jumlah lulus       :",lst["Keterangan"].count("LULUS"))
print("Jumlah gagal       :",lst["Keterangan"].count("GAGAL"))



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




