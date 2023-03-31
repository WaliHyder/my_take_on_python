#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:58:57 2022

@author: walihyder

"""

import re

months =["January","February","March","April","May","June","July","August","September","October","November","December"]

date_formats= 'format1:031297,format2: 12/12/1996,format3: April 15, 1903'


"""if the date is presented in format1, we need to tranform to the two other formats"""
    
format1 = re.search(r'\d{6}', date_formats)

if format1:
        format1 = format1.group()
        reformat1 = re.findall(r'(\d{2})(\d{2})(\d{2})',date_formats)
        #Assign month,day and year to be used for tranforming into other 2 formats
        month = reformat1[0][0]
        day = reformat1[0][1]
        year = reformat1[0][2]
        # Tranform into other two formats and print all 3 formats in order 
        format_2 = day + '/' + month + '/' +'19' +year #format 2 
        format_3 = months[int(month)-1] + ' '+ day +','+' 19' + year #format3
        print(format1) 
        print(format_2)  #format2
        print(format_3) #format3
        print()
        
"""if the date is presented in format2, we need to tranform for format 3 and format 1"""
        
        
format2 = re.search('(\d{2})/(\d{2})/(\d{4})', date_formats)

if format2:
        format2 = format2.group()
        reformat2= re.findall(r'(\d{2})/(\d{2})/(\d{2})(\d{2})',date_formats)
        month = reformat2[0][0]
        day = reformat2[0][1]
        year = reformat2[0][3]
        # Tranform into other two formats and print all 3 formats in order 
        format_3 = months[int(month)-1] + ' '+ day +','+' 19' + year #format3
        format_1 = day+month+year #format1
        print(format2)
        print(format_3)
        print(format_1)
        print()

       
#if the date is presented in format3, we need to tranform for format 1 and format 2
    
 
format3 = re.search(r'[A-Z][a-z]+ (\d{2}), (\d{4})',date_formats)


if format3:
        format3 = format3.group()
        reformat3= re.findall(r'([A-Z][a-z]+) (\d{2}), (\d{2})(\d{2})',date_formats)
        month = reformat3[0][0]
        day = reformat3[0][1]
        year = reformat3[0][3]
        # Tranform into other two formats and print all 3 formats in order 
        format_1 ='0' + str(months.index(month)+1)+day+year #format1
        format_2 = '0' + str(months.index(month)+1)+ '/' + day +'/' + '19' + year #format3
        print(format3)
        print(format_1)
        print(format_2)
        print()
