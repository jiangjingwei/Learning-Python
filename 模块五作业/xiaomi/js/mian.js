$(function () {
    $('#slide-menu li').hover(function () {
        $('#product-con').show();
    }, function () {
        $('#product-con').hide();
    });



    $('#container-title li').hover(function () {
        $('#title-slide').show();
    }, function () {
        $('#title-slide').hide();
    });


    $('#search-box').focus(function () {
        $('#search-text').hide();
    });


    $('#search-box').focusout(function () {
        $('#search-text').show();
    });



});