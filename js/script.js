function createTaskTextInputItem(text, name) {
    var input = $('<input type="text" name=' + name.toLowerCase() + '>').val(text);
    return $('<div></div>').append(name).append(input);
}

function createTaskToggleInputItem(val, name) {
    var input = $('<input type="checkbox" name=' + name.toLowerCase() + '>').val(val);
    $(input).prop("checked", val);
    return $('<div></div>').append(name).append(input);
}

function createCopyButton() {
    var button = $('<button>Copy</button>');

    $(button).click(function(e) {
        var template = $(e.target).parent().parent()[0];

        $('.taskList').append($(template).clone());
    });

    return button;
}

function createTaskItem(task) {
    var text = task.task + ", " + task.title + ", " + task.schedule;
    var form = $('<div></div>'
            ).addClass('task-item'
            ).append(createTaskTextInputItem(task.title, 'Title')
            ).append(createTaskTextInputItem(task.task, 'Type')
            ).append(createTaskTextInputItem(task.schedule, 'Schedule'))

    if(task.args) {
        form.append(createTaskTextInputItem(task.args.slice(1), 'Args'));
        form.append(createTaskToggleInputItem(task.args[0], 'Active'));
    }

    form.append(createCopyButton());

    var ele = $("<li></li>"
        ).addClass('task-list'
        ).append(form);

    return ele;
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

            if(key === "active") {
                console.log($(inputItems[j]));
                args[key] = $(inputItems[j]).context.checked;
            } else if(key === "args") {
                args[key] = val.split(",");
            } else {
                args[key] = val;
            }
        }

        if(args['args']) {
            args['args'].unshift(args['active']);
        }

        tasks.push(args);
    }

    $.post('/createConfig', {
        tasks: JSON.stringify(tasks)
    }, function(res) {
        console.log(res);  
    });
});
