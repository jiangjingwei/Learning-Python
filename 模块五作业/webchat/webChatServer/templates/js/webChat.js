$(function (){


    // 隐藏登陆框
    if($.cookie('loginFlag')){
        $('.login-wrap').hide();
        console.log($.cookie('loginFlag'));

    }else {
        $('.login-wrap').fadeIn(1000);
    };



    // 点击按钮登陆
    $('#login-btn').click(function () {
       var username = $('#username').val();
       var password = $('#password').val();
       // console.log(username,password)


       login(username,password);

    });

    // 每个好友点击跳转聊天页面
    $(".center-wrap").on('click', '.chat-item', function () {
        console.log(111);
        var user = $(this).children('.item').children('h3').text();

        var url = 'http://localhost:9999/chat.html?user=' + user;

        window.location.replace(url);


    });


    $('#send-btn').click(function () {
        // console.log($('#send-content').val());
        var content = $('#send-content').val();
        var $p = $('<p>').addClass('fr').text(content);
        var $div = $('<div>').append($p);
        $('.chat-center-wrap').append($div);


        var datamessage = {sendUser:$.cookie('loginFlag'), recvUser:$('#user').text(), message:content};
        // console.log(datamessage)

        $.post({
            url:'/webchat',
            type:'json',
            data:datamessage,
            success:function (data) {
                console.log('callback', JSON.parse(data))
            }
        })
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