$(function () {

    // 添加todo
    $('#add-btn').click(function () {
        var $input_con = $('#input-con');


        if($input_con.val() === ''){
            return
        }


        var content = $input_con.val() + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';
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
        var $li = $(this).attr({class:'glyphicon glyphicon-ok', id:'transfer'}).siblings().attr({id:'remove'}).parent();
        $li.remove();
        $doing.append($li)

    });

    //  编辑todo

    $('#row').on('click', '.edit', function () {

        var $current_node = $(this).parent();

        console.log($current_node);



        if($current_node.parent().attr('id') === 'doing'){
            console.log(111);

            $('#save').click(function () {

                console.log(222);


                var $edit = $('#edit-con');

                if($edit.val() === ''){return}

                // var edit_content = $edit.val() + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';
                var edit_content = $edit.val() + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';

                $current_node.html(edit_content);

                $edit.val('');


            })

        }


        if($current_node.parent().attr('id') === 'done'){
            console.log(333);
            $('#save').click(function () {
                var $edit = $('#edit-con');

                 console.log(444);

                if($edit.val() === ''){return}

                // var edit_content = $edit.val() + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';
                var edit_content = $edit.val() + '<span class="glyphicon glyphicon-remove" id="remove1"></span><span class="glyphicon glyphicon-share-alt" id="reset"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';

                $current_node.html(edit_content);

                $edit.val('');


            })


        }



        // $('#save').click((function (node) {

            // var $edit_value = $('#edit-con').val();

            // console.log(node.attr('id'));




                // if($edit.val() !== ''){
                //     console.log(111);

                 // console.log($current_node.parent());



                // console.log($edit_value)





                 // var edit_content =  $edit.val() + '<span class="glyphicon glyphicon-remove" id="remove"></span><span class="glyphicon glyphicon-ok" id="transfer"></span><span class="glyphicon glyphicon-pencil edit" data-toggle="modal" data-target=".bs-example-modal-lg"></span>';
                 //
                 //
                 // $current_node.html(edit_content);
                 //
                 // $edit.val('');

            // }

        // })($current_node.parent()));


    })





});
