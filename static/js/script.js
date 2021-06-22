function authorize() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        if (this.responseText == "") {
          console.log(this.responseText)
          alert("로그인 상태가 아닙니다. 로그인을 다시 해주세요.")
          location.href = "signinpage"
        };
      };
    };
    token = localStorage.getItem("access_token");
    xhttp.open("POST", "user_only");
    xhttp.setRequestHeader("Authorization", "Bearer " + token);
    xhttp.send();
  }