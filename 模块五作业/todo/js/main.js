$(function () {



    //  清空

    $('#clear-btn').click(function () {

        $('#row li').remove();
    });

    // 添加todo
    $('#add-btn').click(function () {
        var $input_con = $('#input-con');


        if($input_con.val() === ''){
            return
        }

        // var $div = $('<div>').text();

        var content = '<div>'+ $input_con.val() +'</div>' + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';
        var $li = $('<li>').addClass('list-group-item');

        $li.html(content);

        $('#doing').append($li);
        $input_con.val('')

    });

    var $doing = $('#doing');

    var $done = $('#done');


    // 完成todo
    $doing.on('click', '#transfer', function () {
        var $li = $(this).attr({class:'glyphicon glyphicon-share-alt', id:'reset'}).prev().attr({id:'remove1'}).parent();
        $li.remove();
        $done.append($li);

    });


    // doing删除todo
    $doing.on('click', '#remove', function () {
        $(this).parent().remove()
    });

    // done删除todo
    $done.on('click', '#remove1', function () {
        $(this).parent().remove()
    });


    // 重置todo

    $done.on('click', '#reset', function () {
        var $li = $(this).attr({class:'glyphicon glyphicon-ok', id:'transfer'}).prev().attr({id:'remove'}).parent();
        $li.remove();
        $doing.append($li)

    });

    //  编辑todo

    current_node = null;

    $('#row').on('click', '.edit', function () {
        $('#edit-con').val('');
        // console.log($(this).parent().text());
        current_node = $(this).parent();
    });


    $('#save').click(function () {
        // console.log($('#edit-con').val());
        var edit_value = $('#edit-con').val();
        console.log(current_node.children('div'));
        current_node.children('div').text(edit_value);
        current_node = null;
    })


});
