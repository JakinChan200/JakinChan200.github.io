function onLoginClick() {
    var user = document.getElementById("username").value;
    var pw = document.getElementById("password").value;
    if (user.length > 0 && pw.length > 0) {
        window.location.href = "login-home.html";
    } else {
        document.getElementByID("wrong-pw").innerHTML = "Wrong username and/or password!"
    }
}
