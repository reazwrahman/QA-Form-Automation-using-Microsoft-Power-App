#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:19:06 2020

TC ELECTRIC LLC

@author: Reaz
"""

import pandas as pd 
import os,re,sys



class power_app_code(object): 
    
    def __init__(self,code_file,excel_file): 
        
        self.job_number=[] 
        self.job =[]  
        self.logo=[] 
        self.logo_map={'TC Electric':100,'Judlau Enterprise':200,'JTTC':300,'TCJT':400} 
        #self.logo_map is a hashmap for storing the integer value of each logo type
    
        self.excel_file=excel_file
        self.code_file=code_file 
    
    
    def writer (self,filename,content):   
        
        with open(filename,"w") as file: 
            file.write(content) 
        
#        file=open(self,filename,'w') 
#        file.write(content) 
#        file.close()
    
    def reader(self,filename): 
        
        file=open(filename,"r") 
        content=file.read() 
        file.close()
        return content
        
    
    def appender (self,filename,content):  
        
        file=open(filename,'a') 
        file.write(content) 
        file.close()  
     
        
    def create_list_from_excel(self): 
        
            
        df=pd.read_excel(self.excel_file) 
        
        columns=list(df.columns) 
        self.job_number=list(df[columns[1]])
        self.job=list(df[columns[0]])   
        self.logo=list(df[columns[2]]) 
        
    def stringify_job_number(self):  
        
        if len(self.job)==0 or len(self.job_number) or len(self.logo)==0: 
            self.create_list_from_excel()
    
            
        self.writer(self.code_file,'[') 
#        self.appender(self.code_file,'" "') 
#        self.appender(self.code_file,',')
        for x in self.job_number: 
            self.appender(code_file,'"')
            self.appender(code_file,x) 
            self.appender(code_file,'"') 
            self.appender(code_file,",") 
        
        self.appender(code_file,']') 
        self.appender(code_file,"\n")   
        self.appender(code_file,"\n")  
        
       
        
    def stringify_job(self,which_job):  
        
        ## which job is going to vary with  
        # create, edit and upload 
        #create=job 
        #edit=job_2 
        #upload=job_1
         
        if len(self.job)==0 or len(self.job_number) or len(self.logo)==0: 
            self.create_list_from_excel() 
            
        job_str=[] 
        job_str.append(f'If({which_job}.Selected.Value="{self.job_number[0]}","{self.job[0]}",')
        self.appender(self.code_file,f'If({which_job}.Selected.Value="{self.job_number[0]}","{self.job[0]}",')
      
        for i in range(1,len(self.job)):
            job_str.append(f'{which_job}.Selected.Value="{self.job_number[i]}","{self.job[i]}"') 
            
        
        for i in range(1,len(self.job)-1):  
            self.appender(code_file,job_str[i]) 
            self.appender(code_file,',') 
        
        self.appender(code_file,job_str[len(job_str)-1]) 
        self.appender(code_file,')')   
        self.appender(code_file,"\n")   
        self.appender(code_file,"\n")  
      
        
            
    def stringify_logo(self,which_job):  
        ## which job is going to vary with  
        # create, edit and upload 
        #create=job 
        #edit=job_2 
        #upload=job_1
         
        if len(self.job)==0 or len(self.job_number) or len(self.logo)==0: 
            self.create_list_from_excel() 
            
        logo_str=[]
        self.appender(self.code_file,f'If({which_job}.Selected.Value="{self.job_number[0]}","{self.logo_map[self.logo[0]]}",')
      
        for i in range(1,len(self.job)):
            logo_str.append(f'{which_job}.Selected.Value="{self.job_number[i]}","{self.logo_map[self.logo[i]]}"')
        
        for i in range(1,len(self.job)-1):  
            self.appender(code_file,logo_str[i]) 
            self.appender(code_file,',') 
        
        self.appender(code_file,logo_str[len(logo_str)-1]) 
        self.appender(code_file,')')  
        self.appender(code_file,"\n")   
        self.appender(code_file,"\n")  
            
            
   

excel_file='TC Job Listing_second.xlsx' 
#excel_file='experimental.xlsx'
code_file='power_app_code.txt' 


 
a=power_app_code(code_file,excel_file) 
a.stringify_job_number() 

#create new report  
a.stringify_job('job') 
a.stringify_logo('job')

#edit existing report
a.stringify_job('job_2') 
a.stringify_logo('job_2') 

#upload report
a.stringify_job('job_1') 
a.stringify_logo('job_1')
    
    
