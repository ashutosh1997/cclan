/**
 * Created by ASHUTOSH on 07-Mar-17.
 */

var uname = document.getElementById('uname'),
    email = document.getElementById('email'),
    psw = document.getElementById('psw'),
    psw2 = document.getElementById('psw2'),
    error = document.querySelectorAll(".error"),
    modal = document.getElementById('myModal'),
    str=document.getElementById('warnText'),
    close = document.getElementsByClassName("close")[0],
    css = "0 0 0 0 #000";
    str.innerHTML="",
    arr = [uname,email,psw,psw2,firstname,fname,mname,nation,
            addr,zip,mob,fbname,enrol,inst,textarea,sname,semail];
var i,count=0;

function clearInput(i) {
	error[i].style.display="none";
	arr[i].style.boxShadow = css;
}
	
function check(s) {

    var css = "0 0 20px 3px red";
    if(s==0)
    {   count=0;
        for (i=0;i<=3;i++)
        if (arr[i].value.length==0) {
            error[i].style.display="block";
            arr[i].style.boxShadow = css;
            arr[i].setCustomValidity(" ");
            count++;
        }
        if (count==0)
        {
            var len = email.value.length,
                index = email.value.lastIndexOf('.');
            if(uname.value.match(/^\s*$/))
                str.innerHTML+="Username is invalid.<br>";
            for (var i=0,j=0; i<email.value.length; i++)
                if(email.value[i]=='@')
                    j=i;
            if (j==0 || len-j+1<3 || index<j || index==len-1)
                str.innerHTML+="Email address is invalid (should be of the type someone@xyz.com).<br>";
            if (psw.value!=psw2.value)
                str.innerHTML+="Passwords don't match, please re-enter password.<br>";
            if (str.innerHTML!="")
                modal.style.display = "block";
        }
    }

    //else return true;
}

close.onclick = function() {
    modal.style.display = "none";
    str.innerHTML="";
};
document.getElementById('ok').onclick = function() {
    modal.style.display = "none";
    str.innerHTML="";
};
