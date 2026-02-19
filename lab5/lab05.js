
function nameChecker(){
    let name = document.getElementById('name').value.trim();
    if (name.length === 0){
        return false;
    }
    for (let i = 0; i<name.length; i++){
        let ch = name[i].toLowerCase();

        if (ch < 'a' || ch > 'z'){
            return false;
        } 
    } 
    return true;
}

function phoneChecker(){
    let phone = document.getElementById('phone').value;

    if (phone.length < 14) {
        return false
    }

    for (let i = 0; i < phone.length; i++){

        if (i === 0 && phone[i] != '(' ){
            return false;
        }else if (i === 4 && phone[i] != ')'){
            return false;
        }else if (i === 5 && phone[i] != ' '){
            return false;
        }else if (i === 9 && phone[9] != '-'){
            return false;
        }else if ((i >= 1 && i <= 3) || (i >= 6 && i <= 8) || (i >= 10 && i <= 13)){
            if (phone[i] < '0' || phone[i] > '9'){
                return false;
            }
        }
    }

    return true;
}

function addressChecker(){
    let address = document.getElementById('address').value;
    
    if (address.length === 0){
        return false;
    }
    return true;
}

function formatNumber(){
    let phone = document.getElementById('phone').value.trim();

    let newPhone = "";

    for (let i = 0; i < phone.length; i++){
        let ch = phone[i];
        if (newPhone.length === 3){
            newPhone += '-'
        }
        if (ch === '(' || ch === ')' || ch === ' '){
            continue
        }else{
            newPhone += ch;
        }
    }

    return newPhone;
}

function displayInfo(){
    let address = document.getElementById('address').value;
    let name = document.getElementById('name').value.trim();    
    let phone = formatNumber();

    let outputHTML = `
        <p><strong>Name: </strong>${name}</p>
        <p><strong>Address: </strong>${address}</p>
        <p><strong>Phone Number: </strong>${phone}</p>
    `;

    let outputDiv = document.getElementById('output');

    outputDiv.innerHTML += outputHTML;

}


function validateAll(){
    if (!nameChecker()){
        window.alert("Invalid Name. Name should only contain letters")
    }else if (!addressChecker()){
        window.alert("Address field can't be left empty")
    }else if (!phoneChecker()){
        window.alert("Make sure your phone number is in correct format: (012) 345-6789")
    }else{
        displayInfo();
    }
}


function updateClock(){
    const timeNow = new Date();

    let hours = timeNow.getHours();
    let min = timeNow.getMinutes();
    let seconds = timeNow.getSeconds();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (min < 10) {
        min = "0" + min;
    }

    if (seconds < 10){
        seconds = "0" + seconds;
    }

    const timestr = `${hours}:${min}:${seconds}`;

    let clock = document.getElementById('clock');
    clock.innerHTML = timestr;
}


$(document).ready(function (){
    

    $("#catPic").click(function () {
        $(this).animate({width: "380px", opacity: 0.8}, 300);
        $(this).css({
            "transform": "scale(1.5)"
        });
        $("#pictureText").css({"opacity":"0.8"});
        $("#smallButton").css({"opacity":"1"});
        $('#pictureText').arctext({radius: 600, dir: -1});

    });

    



    $("#smallButton").click(function() {
        $("#catPic").animate({width: "300px", opacity: 1}, 500);
        $("#catPic").css({
            "transform": "scale(1)"
        });
        $("#pictureText").css({"opacity":"0"});
        $("#smallButton").css({"opacity":"0"});
    });

    
});

updateClock()
setInterval(updateClock, 1000)