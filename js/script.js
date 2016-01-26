function createTaskInputItem(text, name) {
    return $('<div></div>').append(name + '   <input type="text" name=' + name + ' value=' + text + '>');
}

function createTaskItem(task) {
    var text = task.task + ", " + task.title + ", " + task.schedule;
    return $("<li></li>"
        ).addClass('task-list'
        ).append($('<div></div>'
            ).addClass('task-item'
            ).append(createTaskInputItem(task.title, 'Title')
            ).append(createTaskInputItem(task.task, 'Type')
            ).append(createTaskInputItem(task.schedule, 'Schedule')
            ).append(createTaskInputItem(task.args, 'Args'))
        );
}

$.get('/tasks', function(data) {
    var list = $('.taskList')[0];

    for(var i = 0; i < data.tasks.length; i++) {
        var task = data.tasks[i];
        $(list).append(createTaskItem(task));
    }
    console.log(data);
});
