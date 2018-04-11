$(function (){




    $('#login-btn').click(function () {
       var username = $('#username').val();
       var password = $('#password').val();
       // console.log(username,password)


       login(username,password);



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

                // console.log('code:', JSON.parse(data));
                if(data.code[0] === 1){
                    console.log('login success');

                    setTimeout(function () {
                        toast5.update({
                            infoIcon: 'images/success.png',
                            infoText: '登陆成功',
                            autoClose: 2500,
                        });
                    }, 1000);

                    //登陆成功后隐藏弹框
                    $('.login-wrap').fadeOut(2000);



                    // $('<div>').appendTo('.center-wrap').addClass('chat-item').html('111')




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
        })

        return 1

    }



});