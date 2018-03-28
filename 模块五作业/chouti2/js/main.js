window.onload = function () {
    var oShoutOff = document.getElementById('shout-off');
    
    oShoutOff.onclick=function () {
        var oPopContainer = document.getElementById('pop_container');
        oPopContainer.style.display = 'none';
    }
};