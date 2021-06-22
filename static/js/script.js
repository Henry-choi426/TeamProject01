function auth() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText)
            console.log(typeof(this.responseText))
            alert("Hello"+this.responseText+"!!")
        };
    }
    token = localStorage.getItem("access_token");
    xhttp.open("POST", "user_only");
    xhttp.setRequestHeader("Authorization", "Bearer "+token);
    xhttp.send();
}
