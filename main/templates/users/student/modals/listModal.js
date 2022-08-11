<script>
$('#submit').on('click', function(){
	var studentgroups = $('#group_select').val();
	var username = $('#username').val();
	var first_name = $('#first-name').val();
	var last_name = $('#last-name').val();
	var birthday = $('#date').val();
	var gender = $('#gender').val();
	var email = $('#email').val();
	var password = $('#password').val();
	var phone = $('#phone').val();
	var father_name = $('#father_name').val()
	$.ajax({
		type:'POST',
		url: '/api/v1/user/student/create/',
		data: {
			studentgroups:studentgroups,
			gender: gender,
			username:username,
			first_name:first_name,
			last_name:last_name,
			birthday:birthday,
			password:password,
			email:email,
			phone:phone,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
			father_name:father_name,
		},
		beforeSend: function (xhr) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		},
		success: function(data){
			{% for id in student %}
			window.location = '/user/student-list/{{ id.id }}';
			{% endfor %}

		},
		error: function(data){
			console.log(data.responseJSON.username[0])
		}
	})
});
$('#cancel').on('click', function(){
	$('#username').val("");
	$('#first-name').val("");
	$('#last-name').val("");
	$('#date').val("");
	$('#email').val("");
	$('#password').val("");
	$('#phone').val("");
	$('#father_name').val("")
})
</script>


<script>
	let objects = document.querySelectorAll('#delete')
        for (let item of objects){
		   item.addEventListener('click', function() {
			   get_id(item.dataset.id)
		   })
	   }
	   function get_id(id){
		var table = $('#example').DataTable();
		$('#remove').on('click', function(){
			var user_id = id
			console.log(user_id)
			$.ajax({
				type:'DELETE',
				url:'/api/v1/user/delete/' + id + '/',
				headers: {'X-CSRFToken': csrftoken},
				success: function(data){
					{% for id in student %}
						window.location = '/user/student-list/{{ id.id }}';
					{% endfor %}
				}
			})
		})
	   }
</script>