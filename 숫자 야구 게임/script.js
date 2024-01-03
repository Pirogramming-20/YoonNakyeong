const n1=document.getElementById('number1');
const n2=document.getElementById('number2');
const n3=document.getElementById('number3');
let myNum=[n1,n2,n3];
let gameNum=9; //시도 가능 횟수
n1.focus();
let sNum;
let bNum;
const img=document.getElementById("game-result-img");

const randN1=Math.floor(Math.random()*10);
let randN2;
let randN3;
while (true) {
    randN2=Math.floor(Math.random()*10);
    if (randN1!==randN2){
        break;
    }
}
while (true) {
    randN3=Math.floor(Math.random()*10);
    if ((randN1!==randN3) && (randN2!==randN3)){
        break; 
    }
}
const randNum=[randN1,randN2,randN3]; //랜덤 숫자 생성 성공
console.log(randNum);
const submitBtn=document.querySelector('.submit-button');
const resultBox=document.querySelector('.result-display');
//버튼 비활성화
n1.addEventListener("input",inputField);
n2.addEventListener("input",inputField);
n3.addEventListener("input",inputField);
function inputField() {
    if (n1.value!="" && n2.value!="" && n3.value!="") {
        submitBtn.disabled=false;
    }
    else {
        submitBtn.disabled=true;
    }
}
inputField();
function check_numbers() {
    if (!isNaN(n1.value) && !isNaN(n2.value) && !isNaN(n3.value)){
        myNum=[Number(n1.value),Number(n2.value),Number(n3.value)];
        console.log(myNum);
        gameNum-=1;
        sNum=0;
        bNum=0;
        for (let i=0;i<3;i++){
            if (myNum[i]==randNum[i]) {
                sNum+=1;
            }
        }
        if (myNum[0] == randNum[1]) {
            bNum+=1;
        }
        if (myNum[0] == randNum[2]) {
            bNum+=1;
        }
        if (myNum[1] == randNum[0]) {
            bNum+=1;
        }
        if (myNum[1] == randNum[2]) {
            bNum+=1;
        }
        if (myNum[2] == randNum[0]) {
            bNum+=1;
        }
        if (myNum[2] == randNum[1]) {
            bNum+=1;
        }
        console.log(sNum);
        console.log(bNum);
        //이제 결과창 출력
        let bigBox = document.createElement("div");
        bigBox.className="check-result";
        let leftBox = document.createElement("div");
        leftBox.className="left";
        let rightBox = document.createElement("div");
        rightBox.className="right";
        leftBox.textContent=myNum.join(" ");
        //다 0인 경우
        if (sNum==0 && bNum==0) {
            let zBox=document.createElement("div");
            zBox.className="out num-result";
            zBox.textContent="0";
            bigBox.appendChild(leftBox);
            bigBox.appendChild(document.createTextNode(":"));
            rightBox.appendChild(zBox);
            bigBox.appendChild(rightBox);
        }
        else {
            let sBox=document.createElement("div");
            let bBox=document.createElement("div");
            sBox.className="strike num-result";
            bBox.className="ball num-result";

            rightBox.appendChild(document.createTextNode(sNum));
            sBox.textContent="S";
            rightBox.appendChild(sBox);

            rightBox.appendChild(document.createTextNode(bNum));
            bBox.textContent="B";
            rightBox.appendChild(bBox);  

            bigBox.appendChild(leftBox);
            bigBox.appendChild(document.createTextNode(":"));
            bigBox.appendChild(rightBox);
        }
        resultBox.appendChild(bigBox);
        //게임 이겼을 때    
        if (sNum==3){
            img.src="success.png";
        }        
        if (sNum!=3 && gameNum<=0) {
            img.src="fail.png";
        }
    }        
    n1.value="";
    n2.value="";
    n3.value="";
}