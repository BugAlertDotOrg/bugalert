html_template = """
<!DOCTYPE html>
  <html>

    <head>
      
      <meta charset="utf-8">
      <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
      <meta name="format-detection" content="telephone=no">
      <meta name="x-apple-disable-message-reformatting">

      <title>Bug Alert</title>
      
      <style>

/* /\\//\\//\\//\\/ CLIENT RESETS /\\//\\//\\//\\/ */
    .ExternalClass{
        width:100%;
    }

    .ExternalClass,
    .ExternalClass p,
    .ExternalClass span,
    .ExternalClass font,
    .ExternalClass td,
    .ExternalClass div{
        line-height: 100%;
    }

    h2{
        color:#0066CC !important;
    }

    #outlook a{
        padding:0;
    }

    table{
        mso-table-lspace:0pt;
        mso-table-rspace:0pt;
    }

    img{
        -ms-interpolation-mode:bicubic;
    }

    body{
        -webkit-text-size-adjust:100%;
        -ms-text-size-adjust:100%;
    }

    /* /\\//\\//\\//\\/ RESET STYLES /\\//\\//\\//\\/ */
    body{
        margin:0;
        padding:0;
        background-color: #FFFFFF;
    }

    img{
        border:0 none;
        height:auto;
        line-height:100%;
        outline:none;
        text-decoration:none;
    }

    a img{
        border:0 none;
    }

    .imageFix{
        display:block;
    }
  
    

    table, td{
        border-collapse:collapse;
    }

    #bodyTable{
        height:100% !important;
        margin:0;
        padding:0;
        width:100% !important;
   background-color: #FFFFFF;
    }

  /* /\\//\\//\\//\\/ GENERAL STYLES /\\//\\//\\//\\/ */
  .center{ margin: 0 auto; }
  .left{ float: left; }
  .right{ float: right; }

  .resize800{ width: 800px; }
  .resize700, .preheader{ width: 700px; }
  .resize660{ width: 660px; }
  .resize600{ width: 600px; }

  .width100p{ width: 100%; }

  .width295{ width: 295px; }
  .width419{ width: 419px; }
  .width50{ width: 50px; }
  .width40{ width: 40px; }
  .width24{ width: 24px; }
  .width20{ width: 20px; }

  .height3{ height: 3px; font-size: 3px; line-height: 3px; mso-line-height-rule: exactly; }
  .height5{ height: 5px; font-size: 5px; line-height: 5px; mso-line-height-rule: exactly; }
  .height11{ height: 11px; font-size: 11px; line-height: 11px; mso-line-height-rule: exactly; }
  .height16{ height: 16px; font-size: 16px; line-height: 16px; mso-line-height-rule: exactly; }
  .height30{ height: 30px; font-size: 30px; line-height: 30px; mso-line-height-rule: exactly; }
  .height40{ height: 40px; font-size: 40px; line-height: 40px; mso-line-height-rule: exactly; }
  .height50{ height: 50px; font-size: 50px; line-height: 50px; mso-line-height-rule: exactly; }

  .copy{ font-family: Arial, Helvetica, sans-serif; }

  .text_left{ text-align: left; }
  .text_right{ text-align: right; }
  .text_center{ text-align: center; }

  .preheader .copy{
   font-size: 12px;
   color: #333333;
  }

  .preheader .copy a, .preheader .copy a:visited,
  .preheader .copy a:hover, .preheader .copy a:active,
  .preheader .copy a strong{ color: #333333; }

  .preheader .copy a strong{ font-weight: normal; }

  a:hover, a:active{ text-decoration-color: #83c300; }

  .cp_link { color: #603AA1; }

  .green_bar{ background-color: #83c300; color: #83c300; }

  .hero .copy{
   font-size: 17px;
   color: #333333;
   line-height: 26px;
  }

  .headline1_style,
  .headline2_style{
   font-family: Arial, Helvetica, sans-serif;
   color: #333333;
   font-weight: bold;
   text-align: center;
  }

  .headline1_style{ font-size: 30px; }
  .headline2_style{ font-size: 24px; }

  .headline1_style a, .headline1_style a:visited,
  .headline1_style a:hover, .headline1_style a:active, .headline1_style a strong,
  .headline2_style a, .headline2_style a:visited,
  .headline2_style a:hover, .headline2_style a:active, .headline2_style a strong{
   color: #333333;
   text-decoration: none;
  }
  
  .headline1_rpi_news{
   font-family: Arial, Helvetica, sans-serif;
   color: #333333;
   font-weight: bold;
   text-align: center;
  }

  .headline1_rpi_news{ font-size: 47px; }
  

  .headline1_rpi_news a, .headline1_rpi_news a:visited,
  .headline1_rpi_news a:hover, .headline1_rpi_news a:active, .headline1_rpi_news a strong{
   color: #333333;
   text-decoration: none;
  }  

  .button_style{
   background-color: #13A48E;
   border-radius: 2px;
  }

  .button:hover .button_style{ background-color: #40C6B2; }

  .button_style, .button_style:hover{
   -webkit-transition: .2s background-color ease-in-out;
   -moz-transition: .2s background-color ease-in-out;
   -ms-transition: .2s background-color ease-in-out;
   -o-transition: .2s background-color ease-in-out;
   transition: .2s background-color ease-in-out;
  }

  .button .copy{
   text-align: center;
   font-size: 18px;
   color: #FFFFFF;
  }

  .button .copy a, .button .copy a:visited,
  .button .copy a:hover, .button .copy a:active, .button .copy a strong{
   color: #FFFFFF;
   text-decoration: none;
  }

  .button .copy a strong{ font-weight: normal; }
  
  
   .showcustom{
   visibility: hidden !important;
    opacity: 0 !important;
   display: none !important;
   
   
    }

  .show, .show table, .show tr, .show td, .show img{
   width: 1px;
   height: 1px;
   font-size: 0px;
   line-height: 0px;
   border: 0px;
   visibility: hidden;
   display: block;
   opacity: 0;
   padding: 0;
   margin: 0;
  }

  .show_dbr, .show_dbr table, .show_dbr tr, .show_dbr td, .show_dbr img{
    width: 1px;
    height: 1px;
    font-size: 0px;
    line-height: 0px;
    border: 0px;
    visibility: hidden;
    display: block;
    opacity: 0;
    padding: 0;
    margin: 0;
   }

  .disclaimer .copy{
   font-size: 12px;
   color: #666666;
   text-align: justify;
  }
  

  .disclaimer .copy, .disclaimer .copy a, .disclaimer .copy a:visited,
  .disclaimer .copy a:hover, .disclaimer .copy a:active,
  .disclaimer .copy a strong{
   color: #666666;
  }

  .disclaimer .copy a strong{
   font-weight: normal;
  }
   .tpo_txt_bnr {
    color:#ffffff !important;
    font-family:Arial, Helvetica, sans-serif !important;
    
  }
  .tpo_txt_bnr h2 {
    color:#ffffff !important;
    font-family:Arial, Helvetica, sans-serif !important;
    
  }

 .underline_button:hover .underline_hover{ background-color: #83c300 !important; color: #83c300 !important; }

</style>

<style>
  
  /* /\\//\\//\\//\\/ 800PX BREAKPOINT /\\//\\//\\//\\/ */
  @media only screen and (max-width:800px){
   .resize800{ width: 100% !important; }
  }

  /* /\\//\\//\\//\\/ 700PX BREAKPOINT /\\//\\//\\//\\/ */
  @media only screen and (max-width:700px){
   .resize700, .resize_img, .preheader{ width: 100% !important; }
   .resize_img{ height: auto !important; }
   .stack{ width: 47% !important; }
   .contact1_wrap{ width: 72% !important; }
  }

  /* /\\//\\//\\//\\/ 660PX BREAKPOINT /\\//\\//\\//\\/ */
  @media only screen and (max-width:660px){
   .resize660{ width: 100% !important; }

   .contact1_item, .contact1_wrap{ width: 100% !important; }
   .contact1_item td{ text-align: center !important; }

   .contact_mob_height30{
    height: 30px !important;
    font-size: 30px !important;
    line-height: 30px !important;
   }
  }

  /* /\\//\\//\\//\\/ 600PX BREAKPOINT /\\//\\//\\//\\/ */
  @media only screen and (max-width:600px){
   .resize600{ width: 100% !important; }
  }

  /* /\\//\\//\\//\\/ 500PX BREAKPOINT /\\//\\//\\//\\/ */
  @media only screen and (max-width:500px){

   .font12{ font-size: 12px !important; }
   .width100{ width: 100px !important; }

   .resize500{ width: 100% !important; }

   .preheader, .preheader table, .preheader tr, .preheader td, .preheader img,
   .collapse, .collapse table, .collapse tr, .collapse td, .collapse img{ display: block !important; }

   .hide_text{ font-size: 0 !important; visibility: hidden !important; display: none !important; }
   .show_text{ font-size: 15px !important; visibility: visible !important; }

   .hide, .hide table, .hide tr, .hide td, .hide img{ display: none !important; }

   .preheader, .preheader table, .preheader tr, .preheader td, .preheader img,
   .collapse, .collapse table, .collapse tr, .collapse td, .collapse img,
   .hide, .hide table, .hide tr, .hide td, .hide img{
    visibility: hidden !important;
    height: 0 !important;
    font-size: 0 !important;
    line-height: 0 !important;
    width: 0 !important;
    opacity: 0 !important;

   }

   .showcustom{
   visibility: visible !important;
    opacity: 1 !important;
   margin: 0 !important;
      display: block !important;
   
   
    }

   .show{ width: 82% !important; margin: 0 auto !important; }
   .show table, .show tr, .show td, .show img{ width: 100% !important; }
    
    .show, .show table, .show tr, .show td, .show img{
    height: auto !important;
    visibility: visible !important;
    opacity: 1 !important;
   }
    
    .show100{ width: 100% !important; margin: 0 auto !important; }
   .show100 table, .show100 tr, .show100 td, .show100 img{ width: 100% !important; }
    
    .show100, .show100 table, .show100 tr, .show100 td, .show100 img{
    height: auto !important;
    visibility: visible !important;
    opacity: 1 !important;
   }

   .stack { width: 100% !important; float: none !important; }
   .stack:last-child{ margin-top: 20px !important; }

   .stack_icons_right { float: left !important; width: 250px !important; display: block !important; }

   .mob_center{ margin: 0 auto !important; }

   .resize436{ width: 94% !important; }

   .mob_nav{ width: 14% !important; padding: 0 3% !important; }

   .mob_width100p{ width: 100% !important; }
   .mob_width81{ width: 81px !important; }
   .mob_width3p{ width: 3% !important; }
   .mob_width31p{ width: 31% !important; }

   .mob_height0{
    height: 0px !important;
    font-size: 0px !important;
    line-height: 0px !important;
   }

   .mob_height5{
    height: 5px !important;
    font-size: 5px !important;
    line-height: 5px !important;
   }

   .mob_height16{
    height: 16px !important;
    font-size: 16px !important;
    line-height: 16px !important;
   }

   .mob_height20{
    height: 20px !important;
    font-size: 20px !important;
    line-height: 20px !important;
   }

   .mob_height30{
    height: 30px !important;
    font-size: 30px !important;
    line-height: 30px !important;
   }

   .mob_height40{
    height: 40px !important;
    font-size: 40px !important;
    line-height: 40px !important;
   }

   .mob_width20{ width: 20px !important; }
   .mob_width50{ width: 50px !important; }

   .mob_line_height{ line-height: 16px !important; }

   .mob_font24{ font-size: 24px !important; line-height: 34px !important; }
   .show_headline{ height: auto !important; visibility: visible !important; }

   .show_underline_button_wrapper{ visibility: visible !important; }
   .show_underline_button_wrapper, .show_underling_button{ height: auto !important; }

   .show_underline_button_copy{
    font-size: 18px !important;
    line-height: 18px !important;
   }

   .show_underline_button_pad{
    height: 2px !important;
    font-size: 2px !important;
    line-height: 2px !important;
   }

   .show_underline_hover{
    height: 3px !important;
    font-size: 3px !important;
    line-height: 3px !important;
    background-color: #333333 !important;
    color: #333333 !important;
   }

   .stack_banker_icons{ width: 237px !important; float: none !important; }

   .hidden_button_first,
   .hidden_button_last{
  width: 100% !important;
  height: auto !important;
  display: table !important;
        visibility: visible !important;
  background-color: #6c9f2e !important;
  border-radius: 2px !important;
  padding: 11px 0 !important;
 }
    
 .hidden_button_first_rkt,
   .hidden_button_last_rkt{
  width: 100% !important;
  height: auto !important;
  display: table !important;
        visibility: visible !important;
  background-color: #13A48E !important;
  border-radius: 2px !important;
  padding: 11px 0 !important;
 }
    
   .hidden_button_first_rm,
   .hidden_button_last_rm{
  width: 100% !important;
  height: auto !important;
  display: table !important;
        visibility: visible !important;
  background-color: #83c300 !important;
  border-radius: 2px !important;
  padding: 11px 0 !important;
 } 

    .hidden_button_copy{font-size: 18px !important; line-height: 26px !important;}

 .show_buttons{
  height: auto !important;
     visibility: visible !important;
     opacity: 1 !important;
  width: 100% !important;
  margin: 0 auto !important;  
  display: table !important;
 }

 .cyoa_headline{
  font-size: 14px !important;
  color: #2081BF !important;
  line-height: 18px !important;
 }
    


 .cyoa_copy{
  font-size: 12px !important;
  color: #333333 !important;
  line-height: 16px !important;
 }

 .mob_font11{ font-size: 11px !important; }

 .show_table{
  display: table !important;
  visibility: visible !important;
  height: auto !important;
  opacity: 1 !important;
  }

  .show_table td{
  font-size: 17px !important;
  line-height: 17px !important;
  padding: 10px !important;
  color: #333333 !important;
  }

 .show_table_border{
  border: 1px solid #e5e5e5 !important;
  padding: 10px !important;
  }

  .powerpack_savings{
  font-size: 40px !important;
  color: #00B398 !important;
  line-height: 40px !important;
  }

  .display_block{
  display: block !important;
  }
   
  }
  
  .imageFixGreyBackground{
        display:block;
        background-color: #F7F7F7;
    }

  /* /\\//\\//\\//\\/ 480PX BREAKPOINT /\\//\\//\\//\\/ */
  @media only screen and (max-width:480px){

   .stack_srv{ width: 100% !important; float: none !important; }

    
    
  }
</style>
      </style>
    </head>
    
    <body style="-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;margin: 0;padding: 0;background-color: #FFFFFF;">
      <!-- START BACKGROUND WRAPPER -->
      <table id="bodyTable" border="0" align="center" cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;border-collapse: collapse;margin: 0;padding: 0;background-color: #FFFFFF;height: 100% !important;width: 100% !important;">
       <tr>
        <td valign="top" style="border-collapse: collapse;">

         <!-- START EMAIL WRAPPER -->
         <table class="center resize800" width="800" border="0" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;border-collapse: collapse;margin: 0 auto;width: 800px;">
          <tr>
           <td valign="top" style="border-collapse: collapse;">
             

<!-- RM BLOCK -->
        <!-- START BAR -->
        <table class="center width100p" width="100%" border="0" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;border-collapse: collapse;margin: 0 auto;width: 100%;">
         <tr>
          <td valign="top" class="green_bar height5" style="border-collapse: collapse;height: 5px;font-size: 5px;line-height: 5px;mso-line-height-rule: exactly;background-color: #83c300;color: #83c300;">&nbsp;</td>
         </tr>
        </table>
        <!-- END BAR -->


<!-- HEADER -->

<!-- RM BLOCK -->

<table class="resize432 center" width="415" border="0" cellpadding="0" cellspacing="0" align="center" style="width:415px;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:20px;padding-bottom:0;padding-right:0;padding-left:0;border-width:0;mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;">
  <tr>
          <td colspan="3" valign="top" class="height30" style="border-collapse: collapse;height: 30px;font-size: 30px;line-height: 30px;mso-line-height-rule: exactly;">&nbsp;</td>
         </tr>
    <tr>
    <td valign="top" class="width20" style="border-collapse: collapse;width: 20px;">&nbsp;</td>
      <td valign="top" style="padding-bottom:0;border-collapse:collapse;"><img src="https://bugalert.org/images/bugalert-logo.png" width="100%" height="100%" class="imageFix resize_img" style="-ms-interpolation-mode:bicubic;height:auto;line-height:100%;outline-style:none;text-decoration:none;border-width:0;border-style:none;display:block;" /></td>
      <td valign="top" class="width20" style="border-collapse: collapse;width: 20px;">&nbsp;</td>
  </tr>
    <tr>
    <td colspan="3" valign="top" class="height30" style="border-collapse: collapse;height: 30px;font-size: 30px;line-height: 30px;mso-line-height-rule: exactly;">&nbsp;</td>
  </tr>
</table>
 


<!-- WARNING MESSAGE -->


<!-- CONTENT -->
        <!-- START HERO CONTENT -->
        <table class="center resize700 hero" width="700" border="0" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;border-collapse: collapse;margin: 0 auto;width: 700px;">
         <tr>
          <td valign="top" class="width50" style="border-collapse: collapse;width: 50px;">&nbsp;</td>
          <td valign="top" class="copy" style="border-collapse: collapse;font-family: Arial, Helvetica, sans-serif;font-size: 17px;color: #333333;line-height: 26px;"><!--[if (!mso 9)&(!mso 14) ]><span style="font-family: Arial, Helvetica, sans-serif;"><![endif]-->



The Bug Alert team would like to inform you of a newly-reported vulnerability, <strong>{title}</strong>.
 <br /><br />
<strong>Summary:</strong><br />{summary}
<br /><br />
<strong>Next steps:</strong><br>Visit <a clicktracking="off" href="{url}">{url}</a> for up-to-date vulnerability details. <a clicktracking="off" href="https://github.com/sullivanmatt/bugalert/pulls?q=is%3Apr+in%3Atitle+log4j">Discussion can be found on GitHub.</a>
<br /><br /><br />
<small>Finally:<br />If this notice was valuable to you, consider donating to help cover the costs of infrastructure and telephony services. <a href="https://bugalert.org/content/pages/financial-support.html">More information can be found here.</a></small>

          <!--[if (!mso 9)&(!mso 14) ]></span><![endif]-->
          </td>
          <td valign="top" class="width50" style="border-collapse: collapse;width: 50px;">&nbsp;</td>
         </tr>
         <tr>
          <td colspan="3" valign="top" class="height50" style="border-collapse: collapse;height: 50px;font-size: 50px;line-height: 50px;mso-line-height-rule: exactly;">&nbsp;</td>
         </tr>
        </table>
        <!-- END HERO CONTENT -->


         <!-- START DISCLAIMER -->
        <table class="resize700 center disclaimer" width="700" border="0" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace: 0pt;mso-table-rspace: 0pt;border-collapse: collapse;margin: 0 auto;width: 700px;">
         <tr>
          <td valign="top" class="width45" style="border-collapse: collapse; width: 45px;">&nbsp;</td>
          <td valign="top" class="copy" style="border-collapse: collapse;font-family: Arial, Helvetica, sans-serif;font-size: 10px;color: #333333;text-align: justify;line-height: 14px;"><!--[if (!mso 9)&(!mso 14) ]><span style="font-family: Arial, Helvetica, sans-serif;"><![endif]-->


   
    This notice, which you have previously signed up for, has been provided by Bug Alert.<br><a clicktracking="off" href="https://bugalert.org/content/pages/my-subscriptions.html">Click here to manage your subscriptions or unsubscribe.</a>
   <br /><br />


   
           <!--[if (!mso 9)&(!mso 14) ]></span><![endif]-->
          </td>
          <td valign="top" class="width45" style="border-collapse: collapse; width: 45px;">&nbsp;</td>
         </tr>
         <tr>
          <td colspan="3" valign="top" class="height50" style="border-collapse: collapse;height: 50px;font-size: 50px;line-height: 50px;mso-line-height-rule: exactly;">&nbsp;</td>
         </tr>
        </table>
        <!-- END DISCLAIMER -->
 
           </td>
          </tr>
         </table>
         <!-- END EMAIL WRAPPER -->

       </td>
      </tr>
     </table>
     <!-- END BACKGROUND WRAPPER -->
   </body>

 </html>
"""
