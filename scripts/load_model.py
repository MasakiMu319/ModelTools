import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "source_models/reader-lm-0.5b"


if torch.backends.mps.is_available:
    device = "mps"
else:
    device = "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

html_content = """<!doctype html>
<html lang="en" dir="auto" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" style="background-color: transparent;">
  <head>
    <title>New Pro Feature: Spaces</title>
    <!--[if !mso]><!-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--<![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style type="text/css">
      #outlook a { padding:0; }
      body { margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%; }
      table, td { border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt; }
      img { border:0;height:auto;line-height:100%; outline:none;text-decoration:none;-ms-interpolation-mode:bicubic; }
      p { display:block;margin:13px 0; }
    </style>
    <!--[if mso]>
    <noscript>
    <xml>
    <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml>
    </noscript>
    <![endif]-->
    <!--[if lte mso 11]>
    <style type="text/css">
      .mj-outlook-group-fix { width:100% !important; }
    </style>
    <![endif]-->
    
    
    <style type="text/css">
      @media only screen and (min-width:480px) {
        .mj-column-per-100 { width:100% !important; max-width: 100%; }
      }
    </style>
    <style media="screen and (min-width:480px)">
      .moz-text-html .mj-column-per-100 { width:100% !important; max-width: 100%; }
    </style>
    
    
  
    
    <style type="text/css">

    @media only screen and (max-width:479px) {
      table.mj-full-width-mobile { width: 100% !important; }
      td.mj-full-width-mobile { width: auto !important; }
    }
  
    </style>
     
    <style type="text/css">
.wfix {
          max-width: 2400px !important;
        }
        @media(max-width: 599px) {
          .body-image-mobile-width-600 td { width: 600px !important; }
          .body-image td  { max-width: 100% !important; }
          .body-image img  { box-sizing: border-box; }
          .social-icon-mobile-spacer {
            display: inline-block !important;
          }
        }
    </style>
    <style>
          .wrapper {
            padding: 0 12px;
          }

          /* Superhuman selector */
          .ShadowHTML .wrapper {
            padding: 0 !important;
          }

         
         
  .ShadowHTML .styleUnquotedContent .unquoted-content a[href]:not(.sh-preserve-color), .ShadowHTML .styleUnquotedContent .sh-unquoted-content a[href]:not(.sh-preserve-color), .ShadowHTML .styleQuotedContent .sh-quoted-content a[href]:not(.sh-preserve-color), .ShadowHTML .sh-signature a[href]:not(.sh-preserve-color), .ShadowHTML .Signature-settings a[href]:not(.sh-preserve-color) {
    color: #13343B !important;
  }
  .ShadowHTML .styleUnquotedContent .unquoted-content .opt-in-explanation a[href]:not(.sh-preserve-color), .ShadowHTML .styleUnquotedContent .sh-unquoted-content .opt-in-explanation a[href]:not(.sh-preserve-color), .ShadowHTML .styleQuotedContent .sh-quoted-content .opt-in-explanation a[href]:not(.sh-preserve-color), .ShadowHTML .sh-signature .opt-in-explanation a[href]:not(.sh-preserve-color), .ShadowHTML .Signature-settings .opt-in-explanation a[href]:not(.sh-preserve-color) {
    color: #9ca3af !important;
    font-size: 12px !important;
    line-height: 18px !important;
  }

         
    .ShadowHTML .styleUnquotedContent .unquoted-content *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings *:not(.sh-preserve-line-height) {
      line-height: 24px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content *:not(.sh-preserve-font-size), .ShadowHTML .styleUnquotedContent .sh-unquoted-content *:not(.sh-preserve-font-size), .ShadowHTML .styleQuotedContent .sh-quoted-content *:not(.sh-preserve-font-size), .ShadowHTML .sh-signature *:not(.sh-preserve-font-size), .ShadowHTML .Signature-settings *:not(.sh-preserve-font-size) {
      font-size: 16px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content *:not(.sh-preserve-font-family), .ShadowHTML .styleUnquotedContent .sh-unquoted-content *:not(.sh-preserve-font-family), .ShadowHTML .styleQuotedContent .sh-quoted-content *:not(.sh-preserve-font-family), .ShadowHTML .sh-signature *:not(.sh-preserve-font-family), .ShadowHTML .Signature-settings *:not(.sh-preserve-font-family) {
      font-family: sans-serif !important;
    }
  
    .ShadowHTML .styleUnquotedContent .unquoted-content h1 *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h1 *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content h1 *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature h1 *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings h1 *:not(.sh-preserve-line-height) {
      line-height: 35px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content h1 *:not(.sh-preserve-font-size), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h1 *:not(.sh-preserve-font-size), .ShadowHTML .styleQuotedContent .sh-quoted-content h1 *:not(.sh-preserve-font-size), .ShadowHTML .sh-signature h1 *:not(.sh-preserve-font-size), .ShadowHTML .Signature-settings h1 *:not(.sh-preserve-font-size) {
      font-size: 28px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content h1 *:not(.sh-preserve-font-family), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h1 *:not(.sh-preserve-font-family), .ShadowHTML .styleQuotedContent .sh-quoted-content h1 *:not(.sh-preserve-font-family), .ShadowHTML .sh-signature h1 *:not(.sh-preserve-font-family), .ShadowHTML .Signature-settings h1 *:not(.sh-preserve-font-family) {
      font-family: sans-serif !important;
    }
  
    .ShadowHTML .styleUnquotedContent .unquoted-content h2 *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h2 *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content h2 *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature h2 *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings h2 *:not(.sh-preserve-line-height) {
      line-height: 30px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content h2 *:not(.sh-preserve-font-size), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h2 *:not(.sh-preserve-font-size), .ShadowHTML .styleQuotedContent .sh-quoted-content h2 *:not(.sh-preserve-font-size), .ShadowHTML .sh-signature h2 *:not(.sh-preserve-font-size), .ShadowHTML .Signature-settings h2 *:not(.sh-preserve-font-size) {
      font-size: 24px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content h2 *:not(.sh-preserve-font-family), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h2 *:not(.sh-preserve-font-family), .ShadowHTML .styleQuotedContent .sh-quoted-content h2 *:not(.sh-preserve-font-family), .ShadowHTML .sh-signature h2 *:not(.sh-preserve-font-family), .ShadowHTML .Signature-settings h2 *:not(.sh-preserve-font-family) {
      font-family: sans-serif !important;
    }
  
    .ShadowHTML .styleUnquotedContent .unquoted-content h3 *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h3 *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content h3 *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature h3 *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings h3 *:not(.sh-preserve-line-height) {
      line-height: 25px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content h3 *:not(.sh-preserve-font-size), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h3 *:not(.sh-preserve-font-size), .ShadowHTML .styleQuotedContent .sh-quoted-content h3 *:not(.sh-preserve-font-size), .ShadowHTML .sh-signature h3 *:not(.sh-preserve-font-size), .ShadowHTML .Signature-settings h3 *:not(.sh-preserve-font-size) {
      font-size: 20px !important;
    }
    .ShadowHTML .styleUnquotedContent .unquoted-content h3 *:not(.sh-preserve-font-family), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h3 *:not(.sh-preserve-font-family), .ShadowHTML .styleQuotedContent .sh-quoted-content h3 *:not(.sh-preserve-font-family), .ShadowHTML .sh-signature h3 *:not(.sh-preserve-font-family), .ShadowHTML .Signature-settings h3 *:not(.sh-preserve-font-family) {
      font-family: sans-serif !important;
    }
  
    .styleUnquotedContent .unquoted-content *:not(.sh-preserve-font-size) h1 *, .styleUnquotedContent .sh-unquoted-content *:not(.sh-preserve-font-size) h1 *, .styleQuotedContent .sh-quoted-content *:not(.sh-preserve-font-size) h1 *, .sh-signature *:not(.sh-preserve-font-size) h1 *, .Signature-settings *:not(.sh-preserve-font-size) h1 * {
      font-size: 28px !important;
    }

    .ShadowHTML .styleUnquotedContent .unquoted-content h1 *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h1 *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content h1 *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature h1 *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings h1 *:not(.sh-preserve-line-height) {
      line-height: 35px !important;
    }
  
    .styleUnquotedContent .unquoted-content *:not(.sh-preserve-font-size) h2 *, .styleUnquotedContent .sh-unquoted-content *:not(.sh-preserve-font-size) h2 *, .styleQuotedContent .sh-quoted-content *:not(.sh-preserve-font-size) h2 *, .sh-signature *:not(.sh-preserve-font-size) h2 *, .Signature-settings *:not(.sh-preserve-font-size) h2 * {
      font-size: 24px !important;
    }

    .ShadowHTML .styleUnquotedContent .unquoted-content h2 *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h2 *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content h2 *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature h2 *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings h2 *:not(.sh-preserve-line-height) {
      line-height: 30px !important;
    }
  
    .styleUnquotedContent .unquoted-content *:not(.sh-preserve-font-size) h3 *, .styleUnquotedContent .sh-unquoted-content *:not(.sh-preserve-font-size) h3 *, .styleQuotedContent .sh-quoted-content *:not(.sh-preserve-font-size) h3 *, .sh-signature *:not(.sh-preserve-font-size) h3 *, .Signature-settings *:not(.sh-preserve-font-size) h3 * {
      font-size: 20px !important;
    }

    .ShadowHTML .styleUnquotedContent .unquoted-content h3 *:not(.sh-preserve-line-height), .ShadowHTML .styleUnquotedContent .sh-unquoted-content h3 *:not(.sh-preserve-line-height), .ShadowHTML .styleQuotedContent .sh-quoted-content h3 *:not(.sh-preserve-line-height), .ShadowHTML .sh-signature h3 *:not(.sh-preserve-line-height), .ShadowHTML .Signature-settings h3 *:not(.sh-preserve-line-height) {
      line-height: 25px !important;
    }
  
         
         
  .ShadowHTML .styleUnquotedContent .unquoted-content .social-icons *:not(.sh-preserve-font-size), .ShadowHTML .styleUnquotedContent .sh-unquoted-content .social-icons *:not(.sh-preserve-font-size), .ShadowHTML .styleQuotedContent .sh-quoted-content .social-icons *:not(.sh-preserve-font-size), .ShadowHTML .sh-signature .social-icons *:not(.sh-preserve-font-size), .ShadowHTML .Signature-settings .social-icons *:not(.sh-preserve-font-size) {
    font-size: unset !important;
  }


          /* Gmail selectors */
          u + .body .wrapper {
            padding: 0 !important;
          }
          div > u + .body .wrapper {
            padding: 0 !important;
          }
          
    a { text-decoration: none; color: #13343B !important; }
    @media (prefers-color-scheme: dark) {
    a { 
    color: #13343B !important;
   }
  }
  
          
    
  .Theme-carbon .divider.dark-force p { border-color: #ffffff !important; }
  .Theme-carbon .powered-by-image-dark { display: block !important; }
  .Theme-carbon .powered-by-image { display: none !important; }
  .Theme-carbon .social-icon.social-icon-hide-dark-mode { display: none !important; }
  .Theme-carbon .social-icon-dark-mode { display: block !important; }
  .Theme-carbon * { color: #ffffff !important; }

    
  .Theme-carbon .styleQuotedContent.styleUnquotedContent .sh-color-grey.link-custom-footer-dark-force, .Theme-carbon .Editor-inner .sh-color-grey.link-custom-footer-dark-force, .Theme-carbon .Signature-settings .sh-color-grey.link-custom-footer-dark-force {
    color: #ffffff !important;
  }

    @media (prefers-color-scheme: dark) {
      
#root[data-shadow-root-container-id] .body { background-color: Canvas !important; }
[class~="x_email-body"] { background-color: #292929 !important; } [class~="x_body"] { background-color: #292929 !important; }
td.dark-force div { color: #FFFFFF !important; }
span.dark-force { color:#FFFFFF !important; }
a.dark-force, a.dark-force span { color: #FFFFFF; }
h1.dark-force, h1.dark-force > span,
h2.dark-force, h2.dark-force > span,
h3.dark-force, h3.dark-force > span { color: #FFFFFF; }
.divider.dark-force p { border-color: #FFFFFF !important; }
.powered-by-image { display: none !important; }
.powered-by-image-dark { display: block !important; }
.social-icon.social-icon-hide-dark-mode { display: none !important; }
.social-icon-dark-mode { display: block !important; }
.link-custom-footer-dark-force { color: #FFFFFF !important; }
.code { background-color: rgb(243, 244, 246, 0.2) !important; }
.powered-by-loops-text a.dark-force, .powered-by-loops-text a.dark-force span { color:#FFFFFF !important; }

    }
          
          .link-unsubscribe { color: #9ca3af !important; }
          </style>
<meta name="color-scheme" content="light dark">
          <meta name="supported-color-schemes" content="light dark">
  </head>
  <body class="body" style="word-spacing:normal;background-color:transparent;">
    
    <div style="display:none;font-size:1px;color:#ffffff;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">Organize your searches + advanced file upload</div>
  
    
      <div class="email-body" style="background-color:transparent;" lang="en" dir="auto">
        <img alt="" src="http://c.vialoops.com/CI0/01000192a2114b68-621bfa73-289b-4b5d-852a-54ddce305531-000000/JV2Jc5vaZkU8rGgUxW2yRbSAKGek5b9qvPlXJcxb0ZQ=375" style="display: none; width: 1px; height: 1px;">
<div style="display: none; max-height: 0px; overflow: hidden;">&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;&#847;&#8203;&nbsp;&#8199;&shy;</div>
        <!--[if mso]><style type="text/css"> a { text-decoration: underline !important; } .button a { text-decoration: none !important; } .outlook-list-fix { margin-left:4px !important; } .outlook-break-full-link { word-break: break-all !important; } .outlook-hide-social-icon { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon * { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon table { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon tbody { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon tr { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon td { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon img { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; } .outlook-hide-social-icon a { display: none !important; mso-hide:all; width: 0px !important; padding: 0px !important; }
</style><table align="middle" border="0" cellpadding="0" cellspacing="0" class="ml-outlook wfix-outlook gmail-no-padding-outlook wrapper-outlook" role="presentation" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    
      
      <div class="ml wfix gmail-no-padding wrapper" style="margin: 0px auto; max-width: 600px; margin-left: 0px !important;">
        
        <table align="middle" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="wfix-outlook" width="600px" ><table align="middle" border="0" cellpadding="0" cellspacing="0" class="wfix-outlook" role="presentation" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    
      
      <div class="wfix" style="margin:0px auto;max-width:600px;">
        
        <table align="middle" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
          <tbody>
            <tr>
              <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0px;padding-left:0px;padding-right:0px;padding-top:0px;text-align:center;">
                <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td align="middle" class="wfix-outlook rounded-corners-outlook styled-primary-column-outlook" style="vertical-align:top;width:600px;" ><![endif]-->
            
      <div class="mj-column-per-100 mj-outlook-group-fix wfix rounded-corners styled-primary-column" style="font-size: 0px; text-align: left; direction: ltr; display: inline-block; vertical-align: top; width: 100%; max-width: 600px !important;">
        
      <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="border-collapse: separate;">
        <tbody>
          <tr>
            <td style="background-color:transparent;border-radius:4px;vertical-align:top;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;">
              
      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%">
        <tbody>
          
              <tr>
                <td align="left" class="body-image body-image-mobile-width-600" style="font-size:0px;padding:10px 25px;padding-top:4px;padding-right:0px;padding-bottom:4px;padding-left:0px;word-break:break-word;">
                  
      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
        <tbody>
          <tr>
            <td style="width:600px;">
              
      <img alt src="https://d3b9kr64nievew.cloudfront.net/cm2b939hy03oe12gcb4ltt5g8/cm2di5ers006pjfbfcenx5t1b.png" style="border:0;border-radius:0px;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="600" height="auto">
    
            </td>
          </tr>
        </tbody>
      </table>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:12px;padding-right:0px;padding-bottom:4px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:28px;line-height:35px !important;text-align:left;color:#13343B;"><h1 class="dark-force" style="padding: 0; margin: 0; font-weight: 500; font-size: 28px; color: #13343B !important; line-height: 35px !important; font-size: 28px !important;"><span style="font-weight: 600; font-size: 28px; white-space: pre-wrap; line-height: 35px !important; font-size: 28px !important;" class="bold">Introducing: Spaces</span></h1></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">We're excited to unveil </span><a target="_blank" rel="noopener noreferrer" class="body-link dark-force" href="https://c.vialoops.com/CL0/https:%2F%2Fperplexity.ai%2Fspaces%3Futm_source=email%26utm_campaign=spaces_launch_101724/1/01000192a2114b68-621bfa73-289b-4b5d-852a-54ddce305531-000000/X_LA4cBZxphZgGoPISIamwt8pSNHRngaIPHkHo_6BhI=375" style="text-decoration: none; color: #13343B !important;"><span style="font-weight: 600; font-size: 16px; white-space: pre-wrap; text-decoration: underline !important; line-height: 24px !important; font-size: 16px !important;" class="bold underline">Spaces</span></a><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;"> — an intuitive way to organize your Threads and, exclusively for Pro subscribers, search your documents and files.</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span>&nbsp;</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:12px;padding-right:0px;padding-bottom:4px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:20px;line-height:25px !important;text-align:left;color:#13343B;"><h3 class="dark-force" style="padding: 0; margin: 0; font-weight: 500; font-size: 20px; color: #13343B !important; line-height: 25px !important; font-size: 20px !important;"><span style="font-weight: 600; font-size: 20px; white-space: pre-wrap; line-height: 25px !important; font-size: 20px !important;" class="bold">Here's what you need to know: </span></h3></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:0;padding-top:0px;padding-right:0px;padding-left:6px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:14.4px;line-height:23.04px;text-align:left;color:#13343B;"><mj-raw>
  <ul style="list-style-type: disc; text-align: left; padding: 0; margin: 0px 0px 2px 26px;">
    <li value="1" class="outlook-list-fix" style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; margin: 0;">
    <span style="font-weight: 600; font-size: 16px; white-space: pre-wrap; line-height: 24px !important; font-size: 16px !important;" class="bold">Collections are now Spaces</span><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">: All your existing Collections are still here, now with a new name and enhanced features.</span>
    </li>
  </ul>
  </mj-raw></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:0;padding-top:0px;padding-right:0px;padding-left:6px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:14.4px;line-height:23.04px;text-align:left;color:#13343B;"><mj-raw>
  <ul style="list-style-type: disc; text-align: left; padding: 0; margin: 0px 0px 2px 26px;">
    <li value="2" class="outlook-list-fix" style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; margin: 0;">
    <span style="font-weight: 600; font-size: 16px; white-space: pre-wrap; line-height: 24px !important; font-size: 16px !important;" class="bold">Organize your threads.</span><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;"> Planning a trip, preparing for an exam, or researching a specific topic? You can now group your Threads into a Space to keep your knowledge organized. </span>
    </li>
  </ul>
  </mj-raw></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:0;padding-top:0px;padding-right:0px;padding-left:6px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:14.4px;line-height:23.04px;text-align:left;color:#13343B;"><mj-raw>
  <ul style="list-style-type: disc; text-align: left; padding: 0; margin: 0px 0px 2px 26px;">
    <li value="3" class="outlook-list-fix" style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; margin: 0;">
    <span style="font-weight: 600; font-size: 16px; white-space: pre-wrap; line-height: 24px !important; font-size: 16px !important;" class="bold">Store and search your files</span><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">: Pro users can upload files to a Space. These files are stored and you can return to search through them whenever — no need to re-upload previous files.</span>
    </li>
  </ul>
  </mj-raw></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span>&nbsp;</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">Start using Spaces to organize your research, search files, and get faster, more accurate answers.</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span>&nbsp;</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="middle" class="button" style="font-size:0px;padding:10px 25px;padding-top:4px;padding-right:0px;padding-bottom:4px;padding-left:0px;word-break:break-word;">
                  
      <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
        <tbody>
          <tr>
            <td align="middle" bgcolor="#20808D" role="presentation" style="border:none;border-radius:4px;cursor:auto;mso-padding-alt:12px 
  16px;background:#20808D;" valign="middle">
              <a href="https://c.vialoops.com/CL0/https:%2F%2Fperplexity.ai%2Fspaces%3Futm_source=email%26utm_campaign=spaces_launch_101724/2/01000192a2114b68-621bfa73-289b-4b5d-852a-54ddce305531-000000/AfOOkiHfAuF0xgJMSMma5lYuN0s1nXddC3V0ITu3jrs=375" style="display: inline-block; background: #20808D; font-family: sans-serif; font-weight: normal; margin: 0; text-decoration: none; text-transform: none; padding: 12px 
  16px; mso-padding-alt: 0px; border-radius: 4px; color: #ffffff !important; font-size: 16px !important; line-height: 16px !important;" target="_blank">
                Try Spaces
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span>&nbsp;</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">Stay curious,</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">Eliot at Perplexity</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span>&nbsp;</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span style="font-style: italic; font-size: 16px; white-space: pre-wrap; line-height: 24px !important; font-size: 16px !important;" class="italic">Questions? Check out our </span><a target="_blank" rel="noopener noreferrer" class="body-link dark-force" href="https://c.vialoops.com/CL0/https:%2F%2Fwww.perplexity.ai%2Fhub%2Ffaq%2Fwhat-are-spaces/1/01000192a2114b68-621bfa73-289b-4b5d-852a-54ddce305531-000000/wfDGuJqKoOZfixG0_Tz6NguFECbW7BrAXXbj9maDb6k=375" style="text-decoration: none; color: #13343B !important;"><span style="font-style: italic; font-size: 16px; white-space: pre-wrap; text-decoration: underline !important; line-height: 24px !important; font-size: 16px !important;" class="italic underline">Spaces FAQ</span></a><span style="font-style: italic; font-size: 16px; white-space: pre-wrap; line-height: 24px !important; font-size: 16px !important;" class="italic"> to learn more</span><span style="line-height: 24px !important; font-size: 16px; font-size: 16px !important; white-space: pre-wrap;">.</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:16px;line-height:24px !important;text-align:left;color:#13343B;"><span>&nbsp;</span></div>
    
                </td>
              </tr>
            
              <tr>
                <td align="left" class="dark-force" style="font-size:0px;padding:10px 25px;padding-top:24px;padding-right:0px;padding-left:0px;word-break:break-word;">
                  
      <div style="font-family:sans-serif;font-size:12px;line-height:18px !important;text-align:left;color:#9ca3af;"><span class="opt-in-explanation" style="color: #9ca3af !important; font-size: 12px !important; line-height: 18px !important;">
  You are receiving this email because you opted-in to receive updates from Perplexity<br>
  Perplexity, 115 Sansome St, Suite 900<br>
  <a style="font-weight: 600; color: #9ca3af !important; text-decoration: none !important; font-size: 12px !important; line-height: 18px !important;" href="https://c.vialoops.com/CL0/https:%2F%2Fapp.loops.so%2Funsubscribe%2Fcm2fe4k1701vj0kl0h71r3t8l%2Fa6858eee11eed6cf0456c4ff1d1230c60d2d3f34794d8534cadc7b7bd7356ceb/1/01000192a2114b68-621bfa73-289b-4b5d-852a-54ddce305531-000000/kIc0jjzZmWOuGOsJkH8-rhZ9xSnEVravpg4HFCZezKg=375" target="_blank" rel="noopener noreferrer" class="bold link-unsubscribe">
  Unsubscribe
  </a>
  </span></div>
    
                </td>
              </tr>
            
        </tbody>
      </table>
    
            </td>
          </tr>
        </tbody>
      </table>
    
      </div>
    
          <!--[if mso | IE]></td></tr></table><![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
        
      </div>
    
      
      <!--[if mso | IE]></td></tr></table></td></tr></table><![endif]-->
              </td>
            </tr>
          </tbody>
        </table>
        
      </div>
    
      
      <!--[if mso | IE]></td></tr></table><![endif]-->
    
    
      </div>
    
  </body>
</html>"""

messages = [{"role": "user", "content": html_content}]
input_text = tokenizer.apply_chat_template(messages, tokenize=False)

print(input_text)

inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=1024, temperature=0, do_sample=False, repetition_penalty=1.08)

print(tokenizer.decode(outputs[0]))