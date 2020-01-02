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


function changebg(obj){
    var sp = $(obj).parent();
    $(".panel-body span").css({"background-color":"#fff","color":"#337AB7"});
    $(obj).css({"color":"337AB7"});
    sp.css({"background-color":"black","color":"white"});
}

function view_stocks(cid){
    params = {'cid': cid};
    $.getJSON("ajax_getstocks_by_category", params, function(res){
        $("#category-name").html("<h3>"+res.ah_category+"</h3>");

        tr_str = "<thead><th>编号</th><th>股票</th><th>当前价</th><th>涨幅</th></thead>";
        for(var i=0;i<res.ah_data.length;i++){
            tr_str += "<tr>"
                    + "<td>"+res.ah_data[i][1] +"</td>"
                    + "<td><a href='detail?sid="+res.ah_data[i][2]+"'>"+res.ah_data[i][0]+ "</a></td>"
                    + "<td class='now-price'>"+res.ah_data[i][3] +"</td>"
                    + "<td class='change-price'>"+res.ah_data[i][4] +"%</td>"
                    + "</tr>";
        }
        $("#stocks-info").html(tr_str);

        var cgp = $(".change-price");

        $(".change-price").each(function(){
            change_price = parseFloat($(this).text().split("%")[0]);
            if(change_price<0){
               $(this).css('color', 'green');
            }else{
               $(this).css('color', 'red');
            }
        });
    });
}