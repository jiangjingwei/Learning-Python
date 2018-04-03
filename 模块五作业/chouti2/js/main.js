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
    
    
    // function moving(th, obj) {
    //
    //     obj.animate({top:'-=100', right:'+=20px', fontSize:'+=80', opacity:'-=2'},1000);
    // transition: left 300ms ease,top 300ms ease,font-size 300ms 30ms;
    // }




    // 事件委托
    $('.item_btn').delegate('span', 'click', function (event) {
        if($(this).attr('class').search('vote') !== -1){
            if($(this).index() === 0){
                $(this).addClass('vote-active').next().addClass('span-active');
            }else {
                $(this).addClass('span-active').prev().addClass('vote-active');
            }



        }else if($(this).attr('class').search('comment') !== -1){

            if($(this).index() === 0){
                $(this).addClass('comment-active').next().addClass('span-active');
            }else {
                $(this).addClass('span-active').prev().addClass('comment-active');
            }


        }else if($(this).attr('class').search('collect') !== -1){

            if($(this).index() === 0){
                $(this).addClass('collect-active').next().addClass('span-active');
            }else {
                $(this).addClass('span-active').prev().addClass('collect-active');
            }

        }







    });

});

