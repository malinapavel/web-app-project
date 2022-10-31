function required(){

    var input = document.forms["form1"]["email-sub"].value;
    var text = document.getElementById("thanks");

    if(input.trim() == "" || input.trim() == null){

        text.style.display = "none";

    }
    else{

        text.style.display = "block";
        
    }
    return false;

}



/*function toggleText() {
    var text = document.getElementById("thanks");
    if (text.style.display === "none") {
        text.style.display = "block";
    } else {
        text.style.display = "none";
    }
}*/