<script>
$('#submit').on('click', function(){
	var name = $('#name').val()
	var description = $('#description').val()
	var owner = $('#owner').val()
	var student = $('#student').val()
	$.ajax({
		type: "POST",
		url: '/api/v1/user/group/create/',
		data:JSON.stringify({
			student:student,
			name:name,
			owner:owner,
			description:description,
			csrfmiddlewaretoken: csrftoken
		}),
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		beforeSend: function (xhr) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		},
		success: function(data){
			window.location = '/user/student-groups'
		},
	})
});
$('#cancel').on('click', function(){
	$('#name').val("")
	$('#description').val("")
	$('#student').val("")
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
			var group_id = id
			console.log(group_id)
			$.ajax({
				type:'DELETE',
				url:'/api/v1/user/group/delete/' + id + '/',
				headers: {'X-CSRFToken': csrftoken},
				success: function(data){
					window.location = '/user/student-groups'
				},
			})
		})
	   }
</script>