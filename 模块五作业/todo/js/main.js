$(function () {

    // 添加todo
    $('#add-btn').click(function () {
        var $input_con = $('#input-con');


        var content = $input_con.val() + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span>';
        var $li = $('<li>').addClass('list-group-item');

        $li.html(content);

        $('#doing').append($li);
        $input_con.val('')

    });

    var $doing = $('#doing');

    var $done = $('#done');


    // 完成todo
    $doing.on('click', '#transfer', function () {
        var $li = $(this).attr({class:'glyphicon glyphicon-share-alt', id:'reset'}).siblings().attr({id:'remove1'}).parent();
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
        var $li = $(this).attr({class:'glyphicon glyphicon-ok', id:'transfer'}).siblings().attr({id:'remove'}).parent();
        $li.remove();
        $doing.append($li)

    });
});
