#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:38:28 2017

@author: Nahid
"""

import numpy as np

fid_import = 'Data.txt'
Import = np.loadtxt(fid_import)

[Row,Col] = Import.shape

if Row % 2 == 0: # For an even number of Rows
    #
    NoOddEvenRows = int((Row/2))

    # Initialize array
    Odd = np.zeros(shape=(NoOddEvenRows,Col))
    Even = np.zeros(shape=(NoOddEvenRows,Col))

    # Loop over odd and even numbers of rows in array
    i_odd = 0
    i_even = 1
    for i in range(0,NoOddEvenRows):
        Odd[i,:] = Import[i_odd,:]
        Even[i,:] = Import[i_even,:]
        i_odd = i_odd + 2
        i_even = i_even + 2
    #end
    
    # Write to text file
    fid1 = 'odd_rows.txt'
    np.savetxt(fid1,Odd,fmt='%1.4e')
    fid2 = 'even_rows.txt'
    np.savetxt(fid2,Even,fmt='%1.4e')
    

elif Row % 2 == 1: # For an odd number of Rows
    #
    NoOddRows = int((Row/2 + 0.5))
    NoEvenRows = Row - NoOddRows 

    # Initialize array
    Odd = np.zeros(shape=(NoOddRows,Col))
    Even = np.zeros(shape=(NoEvenRows,Col))

    # Loop over odd numbers of rows in array
    i_odd = 0
    for i in range(0,NoOddRows):
        Odd[i,:] = Import[i_odd,:]
        i_odd = i_odd + 2
    #end
    # Loop over even numbers of rows in array
    k_even = 1
    for k in range(0,NoEvenRows):
        Even[k,:] = Import[k_even,:]
        k_even = k_even + 2
    #end
    
    # Write array to file
    fid1 = 'odd_rows.txt'
    np.savetxt(fid1,Odd,fmt='%1.4e')
    fid2 = 'even_rows.txt'
    np.savetxt(fid2,Even,fmt='%1.4e')   
#end
