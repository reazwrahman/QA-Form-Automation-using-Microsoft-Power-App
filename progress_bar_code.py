

If(IsBlank(BrowseGallery1),
"No records found with the given selections, 
go back and select 'Search with Just Job Name/Number'",
"Your selections returned the following results")


// code for next button 

UpdateContext({popup:true,cancel:true}); 



If(
progress_1.Text="10%", 
"** One or missing elements  
in the Project Information Section:
    
The following fields are required- 
*Description 
*Work Location
*Work Performed By
*Items Installed 
*Approved by NYCT
*Spec Section  
& Completed by" 
 
    
,progress_1.Text="40%",
"** One or missing elements 

in the Inspection Plan Section:     
Make sure you have answered all the questions 

Valid Answeres are: Yes, No or N/A " 



,progress_1.Text="80%", 
"** One or missing elements  

in the Sign Section:  
The following items are required: 

*QM/QS  
*Date (QM) 
*Date (CCM)"

)








If(Progress.Text="100%",
ClearCollect(
    coltest2,
    {
        contract_no: contract_no.Text,
        description: description.Text,
        work_location: work_location.Text,
        work_performed_by: work_performed_by.Text,
        items_installed: items_installed.Text,
        approved_by: approved_by.Text,
        spec_section: spec_section.Text,
        completed_by: completed_by.Text,
        a1: a1.Selected.Value,
        c1: c1.Text,
        a2: a2.Selected.Value,
        c2: c2.Text,
        a3: a3.Selected.Value,
        c3: c3.Text,
        a4: a4.Selected.Value,
        c4: c4.Text,
        a5: a5.Selected.Value,
        c5: c5.Text,
        a6: a6.Selected.Value,
        c6: c6.Text,
        a7: a7.Selected.Value,
        c7: c7.Text,
        a8: a8.Selected.Value,
        c8: c8.Text,
        a9: a9.Selected.Value,
        c9: c9.Text,
        a10: a10.Selected.Value,
        c10: c10.Text,
        a11: a11.Selected.Value,
        c11: c11.Text,
        a12: a12.Selected.Value,
        c12: c12.Text,
        qm_sign: qm_sign.Text,
        qm_date: qm_date.SelectedDate,
        qm_shift: qm_shift.Selected.Value,
        ccm_sign: ccm_sign.Text,
        ccm_date: ccm_date.SelectedDate,
        ccm_shift: ccm_shift.Selected.Value,
        additional_comment: additional_comment.Text,
        job: job,
        job_number: job_number,
        logo_path:logo_path, 
        file_name:Concatenate(job_number,"-",Text(qm_date.SelectedDate,"[$-en-US]mm_dd_yy"),".html"),
        pdf_name:Concatenate(job_number,"-",Text(qm_date.SelectedDate,"[$-en-US]mm_dd_yy"),".pdf"),
        doc_name:Concatenate(job_number,"-",Text(qm_date.SelectedDate,"[$-en-US]mm_dd_yy"),".doc"),
        weather:Text(weather_info.responses.weather.current.cap),

        u1:If(Text(u1_image.Image)="appres://resources/SampleImage","No Image Uploaded",Substitute(JSON(u1_image.Image,JSONFormat.IncludeBinaryData),"""","")),  
        u2:If(Text(u2_image.Image)="appres://resources/SampleImage","No Image Uploaded",Substitute(JSON(u2_image.Image,JSONFormat.IncludeBinaryData),"""",""))         
    }
); 
text_flow.Run(JSON(coltest2));


Navigate(FinishScreen4NewForm,Fade,{filename:Concatenate(job_number,"-",Text(qm_date.SelectedDate,"[$-en-US]mm_dd_yy"),".doc")});  
 
//Navigate(WelcomeScreen);

,UpdateContext({feedback:true,cancel:true}))






//code for cp1
If(Or( 
    IsBlank(job_name_dos),
    IsBlank(contract_no_dos), 
    IsBlank(weather_dos)),
    
    "0",
    "1")



//code for cp2 

If(Or( 
    IsBlank(description_dos),
    IsBlank(work_location_dos), 
    IsBlank(work_performed_by_dos), 
    IsBlank(items_installed_dos),
    IsBlank(approved_by_dos), 
    IsBlank(spec_section_dos),
    IsBlank(completed_by_dos)    
    
    ),
    
    "0",
    "1")

//code for cp3 

If(Or( 
    q1_dos.Selected.Value="---",  
    q2_dos.Selected.Value="---",  
    q3_dos.Selected.Value="---",  
    q4_dos.Selected.Value="---",  
    q5_dos.Selected.Value="---",  
    q6_dos.Selected.Value="---",  
    q7_dos.Selected.Value="---", 
    q8_dos.Selected.Value="---",  
    q9_dos.Selected.Value="---", 
    q10_dos.Selected.Value="---",  
    q11_dos.Selected.Value="---", 
    q12_dos.Selected.Value="---"),
    "0",
    "1")


//code for cp4 

If(Or( 
      IsBlank(qm_sign_dos), 
      IsBlank(qm_date_dos.SelectedDate),  
      IsBlank(ccm_date_dos.SelectedDate)),
    "0", 
    "1")



//progress X: 
    
//for progress text POSITION 
If(And(cp1d.Text="0",cp2d.Text="0"),187+120,
And(cp1d.Text="1",cp2d.Text="0"),(blue_bar_1.Width*0.1)+120,
And(cp1d.Text="1",cp2d.Text="1",cp3d.Text="0"),(blue_bar_1.Width*0.4)+120,
And(cp1d.Text="1",cp2d.Text="1",cp3d.Text="1",cp4d.Text="0"),(blue_bar_1.Width*0.8)+120, 
And(cp1d.Text="1",cp2d.Text="1",cp3d.Text="1",cp4d.Text="1"),(blue_bar_1.Width*1)+110) 
 


//progress Text 

// for progress text
If(And(cp1d.Text="0",cp2d.Text="0"),"0%",
And(cp1d.Text="1",cp2d.Text="0"),"10%",
And(cp1d.Text="1",cp2d.Text="1",cp3d.Text="0"),"40%", 
And(cp1d.Text="1",cp2d.Text="1",cp3d.Text="1",cp4d.Text="0"),"80%",
And(cp1d.Text="1",cp2d.Text="1",cp3d.Text="1",cp4d.Text="1"),"100%")   



//progress Text boolean table

// for progress text 


   
If(cp_logic.Text="0000","0%",
   cp_logic.Text="0001","10%", 
   cp_logic.Text="0011","40%", 
   cp_logic.Text="0111","80%", 
   cp_logic.Text="1111","100%")
   


//green bar width 
// for green_bar width
If(cp_logic.Text="0000",64,
cp_logic.Text="0001",blue_bar_1.Width*0.1,
cp_logic.Text="0011",blue_bar_1.Width*0.4,
cp_logic.Text="0111",blue_bar_1.Width*0.8, 
cp_logic.Text="1111",blue_bar_1.Width*1)







