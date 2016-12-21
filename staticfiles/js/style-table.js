$(document).ready(function () {
    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
	};
    if(isMobile.any()) {
		$("#flash_01").hide();
    }

    $('#alogin').click(function(){
       $.fn.show_modal('#id01');
    });
    $('#w3-btn-close').click(function(){
        $.fn.close_modal('#id01');
    });
    $('#w3-x-close').click(function(){
        $.fn.close_modal('#id01');
    });

    $('#w3-x-close-signin').click(function(){
        $.fn.close_modal('#id02');
    });

    $('#w3-btn-close-signin').click(function(){
        $.fn.close_modal('#id02');
    });

    $('#signin').click(function(){
        $.fn.close_modal('#id01');
        $.fn.show_modal('#id02');
    });

    $.fn.show_modal = function(id) {
        $(id).show("slow");
    }

    $.fn.close_modal = function(id) {
        $(id).hide("slow");
    }

    $("#login_form").submit(function( event ) {

        var username = $('#username').val();
        var password = $('#password').val();
        $('#username').css({'background-color':'#fff'});
        $('#password').css({'background-color':'#fff'});

        if($.trim(username).length < 1) {
            $('#username').css({'background-color':'red'});
            $('#username').focus();
            return false;
        }
        if($.trim(password).length < 1) {
            $('#password').css({'background-color':'red'});
            $('#password').focus();
            return false;
        }
      /*  else {
           window.location.href ='/userauthenticate/';

            $.ajax({
                type: 'POST',
                url: "/userauthenticate/",
                data: {
                    username: $('#username').val(),
                    password: $('#password').val,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(data, textStatus, jqXHR){
                    alert(data);
                },
                error: function(x) {
                    alert("bad");
                }
            });
        }*/
    });

    var filter = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    $("#login_form_signin").submit(function( event ) {

        var username = $('#username_signin').val();
        var password = $('#password_signin').val();
        var repassword = $('#re_password_signin').val();
        var email = $('#email_signin').val();
        $('#username_signin').css({'background-color' : '#fff'});
        $('#password_signin').css({'background-color' : '#fff'});
        $('#re_password_signin').css({'background-color' : '#fff'});
        $('#email').css({'background-color':'#fff'});
        if($.trim(username).length < 1) {
            $('#username_signin').css({'background-color':'#D2A1A1'});
            $('#username_signin').focus();
            $('#error_message').text("User field is empty!");
            return false;
        }
        else if($.trim(password).length < 1) {
            $('#password_signin').css({'background-color':'#D2A1A1'});
            $('#password_signin').focus();
            $('#error_message').text("Password field is empty!");
            return false;
        }
        else if($.trim(repassword).length < 1) {
            $('#re_password_signin').css({'background-color':'#D2A1A1'});
            $('#re_password_signin').focus();
            $('#error_message').text("Password field is empty!");
            return false;
        }
        else if(repassword != password) {
            $('#re_password_signin').css({'background-color':'#D2A1A1'});
            $('#re_password_signin').focus();
            $('#error_message').text("Passwords is not same!");
            return false;
        }
        else if($.trim(email).length < 1) {
            $('#email_signin').css({'background-color':'#D2A1A1'});
            $('#email_signin').focus();
                 $('#error_message').text("E-mail field is empty!");
            return false;
        }
        else if(!filter.test(email)) {
            $("#email_signin").css({'background-color':'#D2A1A1'});
            $('#error_message').text("Not correct type of e-mail!");
            $('#email_signin').focus();
	        return false;
		}

    });

    $("#alogout").click(function() {
        window.location.href ='/user_logout/';
    });

});