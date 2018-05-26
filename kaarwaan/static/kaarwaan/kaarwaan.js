
function validateNonEmpty (inputField, errorMessage) {
    if(!inputField.value){
        errorMessage.innerHTML = "Please select a value before proceeding";
    }
    else{
        errrorMessage.innerHTML = "";
    }
}

