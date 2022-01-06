

function validateSignup(){
  var firstname = document.getElementById("first_name").value;  //getElement e functie deci treb cu ()
  var lastname = document.getElementById("last_name").value;
  var email = document.getElementById("email").value;
  var password1 = document.getElementById("password1").value;
  var password2 = document.getElementById("password2").value;
  
//   if (firstname== "" || lastname=="" || email=="" || password1=="" || password2=="")
//     {
//         alert("Complete all the fields!")
//     }

//     else if (password1 !== password2)
//     {
//         alert("Password must match the Check Password. ")
//     }
    
//     else 
//     {
        signup()
        alert("You have made an account! YAY")
        // document.location.reload(true)
    // }

}


function signup() {
       const data = {
        firstname: document.getElementById('first_name').value,
        lastname:document.getElementById('last_name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password1').value,
}
    console.log(data)

    url = "http://localhost:5006/users";   //luat de unde dam run la fisierul cu api nu din browser + app route
    params = {
        method: 'POST',
        body: JSON.stringify(data),    //make sure to stringify the body
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',   //make sure to addd the header to the correct content type 
        }
    };
    fetch(url,params)
        .then(ifSuccess)
        .then(newUserCreated)  // functiile aici sunt definite mai jos
        .catch(ifError)
    // document.body.innerHTML= "You have made an account!"

}

function ifSuccess(response) {
    console.log("USER CREATED.");
}

function ifError(err) {
    console.log("Error");
}

function newUserCreated(response) {
    const body = document.querySelector('body');
    const p = document.createElement("p");
    p.innerText = `New user created!! User name: ${response.first_name}. User email ${response.email}`;
    body.appendChild(p);
}


function getusers()
{
    url = "http://127.0.0.1:5006/users";
    response= fetch(url)
    .then (Received)
    .then(Response)
    .catch(Error)
}

function Received(response){
    return response.json();
}

function Response(response){
    console.log(response);
}

function Error(error){
    console.log(error);
}