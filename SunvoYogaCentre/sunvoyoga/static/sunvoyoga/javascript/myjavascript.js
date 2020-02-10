const imgsli=document.querySelectorAll(".imageslideshow.slideimage");
const nextimagedelay=3000;
let currentimagecounter=0;


imgsli[currentimagecounter].style.display="block";
setInterval(nextimage,nextimagedelay);

function nextimage(){
    imgsli[currentimagecounter].style.display="none";
    currentimagecounter=(currentimagecounter+1)%imgsli.length;
    imgsli[currentimagecounter].style.display="block";

  
}



function validateForm()
{
  var x = document.forms["myform"]["email"].value;
  var y = document.forms["myform"]["password"].value;

  var atposition=x.indexOf("@");
  var dotposition=x.lastIndexOf(".");

   if (x == "" )
   {
    alert("please enter email");
    return false;
   }

  if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length)
  {
  alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
  return false;
  }

   if (y == "")
  {
    alert("please enter password");
    return false;
  }

   if (y.length < 0 || y.length >= 18)
  {
    alert("Invalid Length!, Password must greater then 4 and less then 18 in Length.");
    return false;
  }

}






function validate_forsignup_Form()
{
  var e = document.forms["myform"]["email"].value;
  var pw = document.forms["myform"]["password"].value;
  var username = document.forms["myform"]["username"].value;
  var fn = document.forms["myform"]["fname"].value;
  var ln = document.forms["myform"]["lname"].value;
  var rpw = document.forms["myform"]["repassword"].value;

  var atposition=e.indexOf("@");
  var dotposition=e.lastIndexOf(".");


 if (username== "" )
   {
    alert("please enter username");
    return false;
   }

   if (fn== "" )
   {
    alert("please enter First name");
    return false;
   }
   if (ln== "" )
   {
    alert("please enter Last name");
    return false;
   }

   if (e== "" )
   {
    alert("please enter email");
    return false;
   }

  if (atposition<1 || dotposition<atposition+2 || dotposition+2>=e.length)
  {
  alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
  return false;
  }

   if (pw == "")
  {
    alert("please enter password");
    return false;
  }

   if (pw.length < 0 || pw.length >= 18)
  {
    alert("Invalid Length!, Password must greater then 4 and less then 18 in Length.");
    return false;
  }
 if (rpw== "" )
   {
    alert("please enter repeat password ");
    return false;
   }
 if(pw != rpw)
   {
    alert("password not match");
    return false;
   }
}








function validate_for_booking_Form()
{
  var fn = document.forms["myform"]["fname"].value;
  var ln = document.forms["myform"]["lname"].value;
  var email = document.forms["myform"]["email"].value;
  var mn = document.forms["myform"]["mobnumber"].value;
  var gender= document.forms["myform"]["gender"].value;


  var x = document.getElementById("myRadio").required;
  document.getElementById("demo").innerHTML = x;


  var atposition=email.indexOf("@");
  var dotposition=email.lastIndexOf(".");


   if (fn== "" )
   {
    alert("please enter First name");
    return false;
   }
   if (ln== "" )
   {
    alert("please enter Last name");
    return false;
   }
   if (mn== "" )
   {
    alert("please enter mobile number");
    return false;
   }
    if(isNaN(mn))
    {
       alert("Enter numeric value")
       return false;
    }
    if(mn.length<10)
    {
       alert("Enter at least 10 digit")
       return false;
    }

    if (email == "" )
   {
    alert("please enter email");
    return false;
   }

  if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length)
  {
  alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);
  return false;
  }

}
