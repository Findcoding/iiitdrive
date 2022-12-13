function delete_file(file_id, csrf_token) {
	$.post("", {
		delete_id: file_id,
		csrfmiddlewaretoken: csrf_token
	});
}

function restore_file(file_id, csrf_token) {
	$.post("", {
		restore_id: file_id,
		csrfmiddlewaretoken: csrf_token
	});
}
