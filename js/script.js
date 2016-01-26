function createTaskInputItem(text, name) {
    var input = $('<input type="text" name=' + name.toLowerCase() + '>').val(text);
    return $('<div></div>').append(name).append(input);
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

$('#createButton').click(function(e) {
    var taskItems = $('.task-item');
    var tasks = [];

    for(var i = 0; i < taskItems.length; i++) {
        var inputItems = $(taskItems[i]).find('input');
        var args = {};

        for(var j = 0; j < inputItems.length; j++) {
            var key = $(inputItems[j]).attr('name');
            var val = $(inputItems[j]).val();
            args[key] = val;
        }

        tasks.push(args);
    }

    $.post('/createConfig', {
        tasks: JSON.stringify(tasks)
    }, function(res) {
        console.log(res);  
    });
});
