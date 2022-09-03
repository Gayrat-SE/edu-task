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
closeBtn = document.getElementById('closeBtn')
    closeBtn.addEventListener('click', function () {
        document.getElementById('CreateStudentForm').reset();
    })

</script>

<script>
	"group/detail/<int:pk>/"
</script>

<script>
	$('#save').on('click', function(){
		let students = $('#students').val()
		let data = new FormData();
		for (var i=0; i < students.length; i++){
                data.append('student', students[i])
        }
		{% for id in student %}
		fetch('/api/v1/user/group/detail/{{ id.id }}/', {
		method: 'PATCH',
		headers: {
			'X-CSRFToken': csrftoken,
		},
		body:data,
		}).then(response => {
                return response.json();
		}).then(data => {
			window.location = '/user/student-list/{{ id.id }}';
		})
		{% endfor %}

	});
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