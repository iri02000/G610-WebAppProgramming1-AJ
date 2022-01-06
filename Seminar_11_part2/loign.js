
function validateSignup(){
  let email = document.getElementById("email").value;
  let password1 = document.getElementById("password1").value;
  
  if (email=="" || password1=="")
    {
        alert("Complete all the fields!")
    }
    else
    {
        signin()
        alert("You have logged in!")
    }

}


function signin(){
    
}