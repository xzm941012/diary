$(document).ready(function () {

    $('#dbRo1').dbRotate2D();
    $("#ima").hide();

    $("form#form1").submit(function (e) {
        e.preventDefault();
        var username = $("#id_username").val();
        var password = $("#id_password").val();
        if (username == "" || password == "") {
            alert("用户名或密码不能为空");
        }
        $.post("/loginajax/", {'username': username, 'password': password}, function (ret) {
            if (ret["status"] == "fail") {
                alert(ret["msg"]);
            } else if (ret["status"] == "ok"){
                location.reload();
            }
            // $.get("/testsession/", {'username': username, 'password': password}, function (ret) {
            //     alert("123");
            // });
        });
    });

    // $.getJSON("/getalldirys/", function (ret) {
    //     alert(ret["status"]);
    //     $.each(ret["obj"], function (i, field) {
    //         alert(field["fields"]["contants"]);
    //     });
    // });


});
function login1() {
    alert("12");
    return false;
}
