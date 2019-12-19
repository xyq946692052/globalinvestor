$(document).ready(function () {
    var trigger = $('.hamburger'),overlay = $('.overlay'),
        isClosed = false;
        trigger.click(function () {
            hamburger_cross();
    });

    function hamburger_cross() {
         if(isClosed == true) {
             overlay.hide();
             trigger.removeClass('is-open');
             trigger.addClass('is-closed');
             isClosed = false;
         }else {
             overlay.show();
             trigger.removeClass('is-closed');
             trigger.addClass('is-open');
             isClosed = true;
         }
    }
    $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
    });
});


function view_stocks(cid){
    params = {'cid': cid};
    $.getJSON("ajax_getstocks_by_category", params, function(res){
        $("#category-name").html("<h3>"+res.ah_category+"</h3>");

        tr_str = "";
        for(var i=0;i<res.ah_data.length;i++){
            tr_str += "<tr><td><a href='detail?sid="+res.ah_data[i][2]+"'>"+res.ah_data[i][0]+ "</a></td><td>"+res.ah_data[i][1] +"</td></tr>";
        }
        $("#stocks-info").html(tr_str);
    });
}