function createTaskItem(task) {
    var text = task.task + ", " + task.title + ", " + task.schedule;
    return $("<li></li").text(text);
}

$.get('/tasks', function(data) {
    var list = $('.taskList')[0];

    for(var i = 0; i < data.tasks.length; i++) {
        var task = data.tasks[i];
        $(list).append(createTaskItem(task));
    }
    console.log(data);
});
