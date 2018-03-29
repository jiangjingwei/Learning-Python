window.onload = function () {
    var oShoutOff = document.getElementById('shout-off');
    
    oShoutOff.onclick=function () {
        var oPopContainer = document.getElementById('pop_container');
        oPopContainer.style.display = 'none';
    };



    // Timer();

    // timer = setInterval(Timer,1000);

    // clearInterval(timer);


    Timer();
    setInterval(Timer, 1000);



    function Timer() {

        var oDateTime = document.getElementById('date-time');

        var now = new Date();
        var year = now.getFullYear();
        var month = now.getMonth()+1;
        var day = now.getDate();
        var week = now.getDay();
        var hours = now.getHours();
        var minutes = now.getMinutes();
        var second = now.getSeconds();

        var dataTime = year + '-' + fullTime(month) + '-' + fullTime(day) + ' ' + fullTime(hours) + ':' + fullTime(minutes) + ':' + fullTime(second) + '  ' + toWeek(week);


        oDateTime.innerHTML = dataTime;

    };





    function toWeek(num) {

        switch (num){
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

        if(num<10){
            num = '0' + num

        }

        return num
        
    }



};