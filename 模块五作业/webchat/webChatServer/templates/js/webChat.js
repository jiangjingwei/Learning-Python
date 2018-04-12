$(function (){



    if($.cookie('loginFlag')){
        $('.login-wrap').hide();
        console.log($.cookie('loginFlag'));

    }else {
        $('.login-wrap').fadeIn(1000);
    };




    $('#login-btn').click(function () {
       var username = $('#username').val();
       var password = $('#password').val();
       // console.log(username,password)


       login(username,password);

    });


    $(".center-wrap").on('click', '.chat-item', function () {
        console.log(111);
        window.location.replace('http://localhost:9999/chat.html');
    });






    // 验证用户登陆
    function login(username,passwrod) {
        var toast5 = $(document).dialog({
                            type : 'toast',
                            infoIcon: 'images/loading.gif',
                            infoText: '正在加载中',
        });

        $.ajax({
            type:'POST',
            url:'/login',
            data:{user:username,pwd:passwrod},
            success:function (data) {
                data = JSON.parse(data);

                console.log('friends:', data.friends);
                if(data.code[0] === 1){
                    console.log('login success');

                    // 设置cookies
                    $.cookie('loginFlag', username, {expires:7, path:'/'});

                    setTimeout(function () {
                        toast5.update({
                            infoIcon: 'images/success.png',
                            infoText: '登陆成功',
                            autoClose: 2500,
                        });
                    }, 1000);

                    //登陆成功后隐藏弹框
                    $('.login-wrap').fadeOut(2000);

                    window.location.reload()


                    // $.each(data.friends, function (index, value) {
                        // console.log(index, value)



                            // /*'<div class="chat-item">\n' +
                            // '                <img src="./images/359.jpg" alt="">\n' +
                            // '                <div class="item clearfix">\n' +
                            // '                    <h3>大胖</h3>\n' +
                            // '                    <span class="msg">message</span>\n' +
                            // '                    <span class="time">09:12</span>\n' +
                            // '                </div>\n' +
                            // '\n' +
                            // '\n' +
                            // '        </div>';


                        // 图片
                        // var $img = $('<img>').attr('src', './images/359.jpg');
                        //
                        // var $h3 = $('<h3>').text(value.username);
                        //
                        // var $item = $('div').addClass('item').addClass('clearfix').append($h3);
                        //
                        // var $chat_item = $('<div>').addClass('chat-item').append($img).append($item);
                        //
                        // $('.center-wrap').append($chat_item);
                        //
                        // console.log($('.center-wrap'));


                    // });





                }else {
                    console.log('login fail');

                    setTimeout(function () {
                        toast5.update({
                            infoIcon: 'images/fail.png',
                            infoText: '登陆失败',
                            autoClose: 2500,
                        });
                    }, 1000);

                }

            }
        });

        return 1

    }



});