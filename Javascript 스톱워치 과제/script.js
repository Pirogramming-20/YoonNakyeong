const time=document.getElementById('time');
const start=document.getElementById('start');
const timestop=document.getElementById('stop');
const reset=document.getElementById('reset');
const resultBottom=document.getElementById('result-bottom');
const sec=document.getElementById('sec');
const msec=document.getElementById('msec');
const trash=document.getElementById('icon2')
const deleteBtn=document.getElementById('delete-btn')

let newsec=0;
let newmsec=0;
let pastTime;
function showTime() {
    let res=document.createElement('div');
    let resBtn=document.createElement('button');
    let resText=document.createElement('div');
    
    res.id='resbox'
    resBtn.className='resultbtn';
    resText.id='restext';
    resText.textContent=sec.textContent+':'+msec.textContent;
    resBtn.addEventListener('click', function() {
        this.classList.toggle('checked');
    });

    res.appendChild(resBtn);
    res.appendChild(resText);
    resultBottom.appendChild(res);
}
start.onclick=function(){
    pastTime=setInterval(checkTime,10)
}
timestop.onclick=function(){
    clearInterval(pastTime)
    showTime();
}
reset.onclick=function(){
    clearInterval(pastTime)
    newsec=0;
    newmsec=0;
    sec.textContent='00';
    msec.textContent='00';
}
function checkTime() {
    newmsec++;
    if (newmsec<10) {
        msec.textContent='0'+newmsec;
    }
    else {
        msec.textContent=newmsec;
    }    
    if (newmsec>99) {
        newsec++;
        newmsec=0;
        if (newsec<10) {
            sec.textContent='0'+newsec;
        }
        else {
            sec.textContent=newsec;
        }     
    }
}
trash.addEventListener('click', function() {
    document.querySelectorAll('#resbox .checked').forEach(function(btn) {
        btn.parentNode.remove();
    });
});

deleteBtn.addEventListener('click', function() {
    const buttons=document.querySelectorAll('.resultbtn');
    let allChecked = true;

    buttons.forEach(btn => {
        if (!btn.classList.contains('checked')) {
            allChecked = false;
        }
    });
    buttons.forEach(btn => {
        if (allChecked) {
            btn.classList.remove('checked');
        }
        else {
            btn.classList.add('checked');
        }
    });    
    if (allChecked) {
        deleteBtn.style.background = 'none';
    }
    else {
        deleteBtn.style.background = "url('https://api.iconify.design/material-symbols/check.svg') no-repeat center center / contain";
    }
});