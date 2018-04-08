window.onload = function () {

    // 登陆注册弹框关闭按钮
    // var oShoutOff = document.getElementById('shout-off');
    //
    // oShoutOff.onclick = function () {
    //     var oPopContainer = document.getElementById('pop_container');
    //     oPopContainer.style.display = 'none';
    // };
    //
    // // 登陆注册按钮弹出登陆注册弹框
    // var oRegister = document.getElementById('register');
    // var oLogin = document.getElementById('login');
    //
    // oRegister.onclick = function () {
    //     var oPopContainer = document.getElementById('pop_container');
    //     oPopContainer.style.display = 'block';
    // };
    //
    // oLogin.onclick = function () {
    //     var oPopContainer = document.getElementById('pop_container');
    //     oPopContainer.style.display = 'block';
    // };


    // Timer();

    // timer = setInterval(Timer,1000);

    // clearInterval(timer);


    // 页面倒计时

    Timer();
    setInterval(Timer, 1000);


    function Timer() {

        var oDateTime = document.getElementById('date-time');

        var now = new Date();
        var year = now.getFullYear();
        var month = now.getMonth() + 1;
        var day = now.getDate();
        var week = now.getDay();
        var hours = now.getHours();
        var minutes = now.getMinutes();
        var second = now.getSeconds();

        var dataTime = year + '-' + fullTime(month) + '-' + fullTime(day) + ' ' + fullTime(hours) + ':' + fullTime(minutes) + ':' + fullTime(second) + '  ' + toWeek(week);


        oDateTime.innerHTML = dataTime;

    };


    function toWeek(num) {

        switch (num) {
            case 0:
                return '星期天';

            case 1:
                return '星期一';

            case 2:
                return '星期二';

            case 3:
                return '星期三';

            case 4:
                return '星期四';

            case 5:
                return '星期五';

            case 6:
                return '星期六';
        }
    }

    function fullTime(num) {

        if (num < 10) {
            num = '0' + num
        }

        return num
    }

};

$(function () {

    // 实现事件冒泡取消
    $('#register').click(function () {
        $('.pop_container').show();
        return false
    });

    $('#login').click(function () {
        $('.pop_container').show();
        return false
    });

    $('#shout-off').click(function () {
        $('.pop_container').hide();
    });

    $(document).click(function () {
        $('#pop_container').hide();
    });

    $('.pop_con').click(function () {
        return false
    });


    // 点赞

    $('.vote').click(function () {
        if($(this).hasClass('vote-active')){
            $(this).removeClass('vote-active').siblings().removeClass('span-active');
            var $span = $('<span>').addClass('vote-animate').appendTo('body');

            var $voteAnimate = $('.vote-animate');
            var $pos = $(this).offset();
            $voteAnimate.html('-1');
            $voteAnimate.css({position:'fixed', left:$pos.left, top:$pos.top, color:'#9add7f'});

            var times = 1;
            var timer = setInterval(function () {

                times ++;
                if (times >15){
                    clearInterval(timer);
                     $voteAnimate.remove();
                }
                $voteAnimate.animate({left:'+=2', top: '-=5', fontSize: '+=4', opacity:'-=0.08'},30);

            },30)
        }else {
            $(this).addClass('vote-active').siblings().addClass('span-active');

            var $span = $('<span>').addClass('vote-animate').appendTo('body');
            var $voteAnimate = $('.vote-animate');
            var $pos = $(this).offset();
            $voteAnimate.html('+1');
            $voteAnimate.css({position:'fixed', left:$pos.left, top:$pos.top, color:'#9add7f'});

            var times = 1;
            var timer = setInterval(function () {

                times ++;
                if (times >15){
                    clearInterval(timer);
                     $voteAnimate.remove();
                }
                $voteAnimate.animate({left:'+=2', top: '-=5', fontSize: '+=4', opacity:'-=0.08'},30);

            },30)

        }

    });



    // 评论

    $('.comment').click(function () {
        if($(this).hasClass('comment-active')){
            $(this).removeClass('comment-active').siblings().removeClass('span-active');
            $(this).parent().parent().parent().parent()[0].children[2].style.display='none'

        }else {
            $(this).addClass('comment-active').siblings().addClass('span-active');
            $(this).parent().parent().parent().parent()[0].children[2].style.display='block'
        }
    });
    



    // goTop
    $(window).scroll(function () {
         // console.log($(window).scrollTop());

        if($(window).scrollTop() <= 600){
            $('.gotop').hide();
        }else {
            $('.gotop').show();
        }

    });


    // 发布弹框
    $('#release_btn').click(function () {
         $('#pop_new_paper').show();
    });


    $('#paper_shout-off').click(function () {
        $('#pop_new_paper').hide();
    });


    // 发布弹框拖动效果
    $('#paper_title').mousedown(function (event) {
        var old_x = event.clientX;
        var old_y = event.clientY;
        // console.log(old_x,old_y);

        var $pop = $('.new_paper_content').offset();
        var pop_x = $pop.left;
        var pop_y = $pop.top;

        // console.log(current_x,current_y);
        $(document).mousemove(function (event) {
            var new_x = event.clientX;
            var new_y = event.clientY;
            console.log(new_x,new_y);
            $('.new_paper_content').css({left:pop_x + new_x - old_x,top:pop_y + new_y - old_y,
                position:'fixed', cursor:'move', margin:0});
        })
    });

    $('#paper_title').mouseup(function (event) {
        $(document).off('mousemove');
        $('.new_paper_content').css({cursor:'default'})
    });




});

