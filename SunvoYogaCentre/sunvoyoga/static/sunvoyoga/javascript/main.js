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