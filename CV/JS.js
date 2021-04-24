function currentDate(){
    var d = new Date();
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    document.getElementById("currDate").innerHTML=months[d.getMonth()] + ", " + d.getFullYear();
    console.log(d);
    
}
function isEmpty(str) {
    return (!str || str.length === 0 );
}
function MessBox(email,name,msg){
    if(isEmpty(email) || isEmpty(name) || isEmpty(msg)){
        alert("Please fill all fields.");
    }
    else{
    alert("Thank you! I will contact you soon!");
    location.href='../html/cv.html';
    }
}

function copyElementText(id) {
    var text = document.getElementById(id).innerText;
    var elem = document.createElement("textarea");
    document.body.appendChild(elem);
    elem.value = text.replace('Copy Email to clipboard','');
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);
    alert(text.replace('Copy Email to clipboard','')+" copied to clipboard!")
}
