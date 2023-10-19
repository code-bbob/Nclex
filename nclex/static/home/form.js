function SeePw(){

    var password = document.querySelector('[name=password]');
    if(password.getAttribute('type')==='password' && password.value != "") {
    
    password.setAttribute('type', 'text');
    document.getElementById("code").innerText='Hide password';
    document.getElementById("see").style.display ='block';
    document.getElementById("hide").style.display = 'none';
    document.getElementById("hide").style.visibility = 'visible';
    document.getElementById("label").style.top = '-3.1rem';
    document.getElementById("label").style.background = 'white';
    document.getElementById("label").style.fontSize = '0.8rem';
    document.getElementById("label").style.left = '-4.8rem';
    document.getElementById("label").style.fontFamily = 'lato,sans-srif';
    document.getElementById("label").style.padding= '0rem .15rem';
    
    }
     else if(password.getAttribute('type')==='text'){
    
    password.setAttribute('type', 'password');
    document.getElementById("hide").style.display ='block';
    document.getElementById("code").innerText='Show password';
    document.getElementById("see").style.display ='none';
    
     }
    
    }
    
    function hide(){
        var icon = document.getElementById("see");
    if(document.form.password.value.length == 0){
    icon.style.visibility = 'hidden';
    }
     
     else if(document.form.password.value.length <=0)
     {
        icon.style.visibility = 'visible';
     }
    else {
    
        icon.style.visibility = 'visible'
    }
    
    }
    