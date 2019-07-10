# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:01:36 2019

@author: devis
"""

import re
filename = '60008610_prova.txt'
date_reg_exp = re.compile("([0-9]{1}\/[0-9]{2}\/[0-9]{4})")
kwh_reg_exp =  re.compile("([0-9]{5}\.[0-9]{3})")
kw_reg_exp   = re.compile("([0-9]{1}\.[0-9]{3})")
datalist=[]
indexlist=[]
kwhlist=[]
kwlist=[]
j=0
k=0
lines = open("60008610_prova.txt", "r").read().splitlines()
#filename.close()
for i, line in enumerate(lines):
        
        if '-M1 -L' in line:
         if lines[i+2][2].isdigit() or lines[i+2][3].isdigit():
            with open(filename) as fh:
                data = str(fh.readlines()[i+2:i+18])
                matches_list=date_reg_exp.findall(data)
               # print(' IMy index is',matches_list.index(max(matches_list)))
                index1=matches_list.index(max(matches_list))
                max1=max(matches_list)
                indexlist.append(index1)
                datalist.append(max1)
         else:
          print('couldnt find the expression')
        if 'M1 -D -P1' in line:
         if lines[i+2][2].isdigit() or lines[i+2][3].isdigit():
           
             with open(filename) as fh:
                kwh = str(fh.readlines()[i+2:i+18])
                kwhmatches_list=kwh_reg_exp.findall(kwh)
                
                kwhtoappend=kwhmatches_list[indexlist[j]]
                print(j)
                
                kwhlist.append(kwhtoappend)
                j=j+1
         else:
                print('Found command for kwh but not values')
                
        if 'M1 -d -P1' in line:
         if lines[i+2][2].isdigit() or lines[i+2][3].isdigit():
             
             with open(filename) as fh:
                kw = str(fh.readlines()[i+2:i+18])
                kwmatches_list=kw_reg_exp.findall(kw)
                
                kwtoappend=kwmatches_list[indexlist[k]]
                kwlist.append(kwtoappend)
                k=k+1
         else:
                kwlist.append('N_A')
                k=k+1
  
for match in datalist:
  print( match)
for match in kwlist:
  print( match)
for match in kwhlist:
  print( match)

#
