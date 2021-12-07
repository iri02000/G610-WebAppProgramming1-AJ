function ShowAlert(){
    alert (" Warning! You are about to reset your inputs. Are you sure you want to continue?”!")
}

function Congrats(){
    alert(" Congrats! You have just made your account!")
}

function Return(){
    console.log ("Success");
}

function validateForm(){
  var x = document.forms["Myform"]["fname"].value;
  var y = document.forms["Myform"]["email"].value;
  var z = document.forms["Myform"]["password1"].value;
  var w = document.forms["Myform"]["password2"].value;
  
  if (x == "" || x == null) 
  {
      alert("Full Name must be filled out");
       return false;
  }
  else if (y == "" || y == null) 
  {
      alert("Email must be filled out");
       return false;
    }
     else if (z == "" || z == null) 
  {
      alert("Password must be filled out");
       return false;
    }
      else if (w == "" || w == null) 
  {
      alert("Check Password must be filled out");
       return false;
    }
    else 
    {
        ShowAlert()
    }

}
function validateSignup(){
 var x = document.forms["Myform"]["fname"].value;
  var y = document.forms["Myform"]["email"].value;
  var z = document.forms["Myform"]["password1"].value;
  var w = document.forms["Myform"]["password2"].value;

  if (x== "" || y=="" || z=="" || w=="")
  alert("Complete all the fields!")
  else 
  Congrats()
}

let sum=0;
for(let i=1 ;i<51;i++)
{
    sum+=i;
 
}
 console.log ("Sum of all numbers up to 50: " +sum)

const greeting = function greet() {
    console.log('Hey there clicker!');
}

// document.getElementById("signup").onclick = Return()

