# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:58:15 2020

@author: NeoSixMan
"""

import numpy as np
import pandas as pd

insurance = pd.read_csv("insurance.csv") #all data
names = [str(i) for i in range(1, insurance.shape[0]+1)]
insurance['names'] = names
#wishList = pd.DataFrame(columns=insurance.columns)
wishList = pd.read_csv("wish_list.csv") #last my wish lish

command = ''

while(command != 'q'):
        command = input('add (a), see (s), remove (r), exit (q) :')        
        if command == 'a':
            name = str(input('Enter product name:'))
            row = insurance.loc[insurance['names'] == name]
            check = wishList.isin({'names': [name]})
            if check['names'].any(axis=None) == False:
                wishList = wishList.append(row)
            else:
                print('already add')
        elif command == 's':
            print(wishList)
        elif command == 'r':
            name = str(input('Enter remove name:'))
            wishList = wishList[wishList.names != name]
        else:
            print('...')
            
wishList.to_csv('wish_list.csv',index = False)