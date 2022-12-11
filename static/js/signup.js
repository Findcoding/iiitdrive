let container = document.getElementById('container1')

toggle = () => {
	container.classList.toggle('sign-in');
	container.classList.toggle('sign-up');
}


setTimeout(() => {
	container.classList.add('sign-up');
}, 200)


function Validate() {
    var password = document.getElementById("psw").value;
    var confirmPassword = document.getElementById("confirm_psw").value;
    if (password != confirmPassword) {
        alert("Password do not match.");
        return false;
    }
    var sign_up = document.getElementById("sign_up");
    alert("Account successfully created.");
    sign_up.type = "submit"
    return true;
}
