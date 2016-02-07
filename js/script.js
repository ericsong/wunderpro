function createTaskTextInputItem(text, name) {
    var input = $('<input type="text" name=' + name.toLowerCase() + '>').val(text);
    return $('<div></div>').append(name).append(input);
}

function createTaskToggleInputItem(val, name) {
    var input = $('<input type="checkbox" name=' + name.toLowerCase() + '>').val(val);
    $(input).prop("checked", val);
    return $('<div></div>').append(name).append(input);
}

function createTaskItem(task) {
    var text = task.task + ", " + task.title + ", " + task.schedule;
    return $("<li></li>"
        ).addClass('task-list'
        ).append($('<div></div>'
            ).addClass('task-item'
            ).append(createTaskTextInputItem(task.title, 'Title')
            ).append(createTaskTextInputItem(task.task, 'Type')
            ).append(createTaskTextInputItem(task.schedule, 'Schedule')
            ).append(createTaskTextInputItem(task.args.slice(1), 'Args')
            ).append(createTaskToggleInputItem(task.args[0], 'Active'))
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
