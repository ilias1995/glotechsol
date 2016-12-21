$(function(){
	$('#send').click(function() {
		var fields = $('.form-horizontal :input');
		var emptyFields = fields.filter(function() {
			fields.css({'border':'1px solid gray'});
			return $.trim(this.value) === "";
		});
		var name = $('#name').val();
		var email = $('#email').val();
		var subj = $('#subject').val();		
		var msg = $('#message').val();
		if(validate() && emptyFields.length == 1) {			
			$.ajax({
				url: 'send_message.php',
				type: 'POST',
				data: {Name: name, Email: email, Subject: subj, Message: msg},
				success: function(data) {
					clearForm();
					//location.reload();					
					alert('Сообщение успешно отправлено!');					
				},
				error: function() {
					alert('Error');
				}
			});
		}
		else {
			emptyFields.css({'border':'1px solid red'});
			$('#result').text('Please fill all fields');
			//emptyFields.effect('bounce', {times:3},500);
		}		
		
	});
	function validateEmail(email) {
		var re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		return re.test(email);
	}
	function validate() {
		var res = false;
		var email = $("#email").val();		
		if (validateEmail(email)) {
			$("#email").css({'border':'1px solid gray'});
			res = true;
		} else {		
			$("#email").css({'border':'1px solid red'});
			res = false;
		}
		return res;
	}
	
	function clearForm()
	{
		$('#name').val("");
		$('#email').val("");
		$('#subject').val("");
		$('#message').val("");
		$('#result').text('');
	}
	
});
