$(document).ready(function() {
    $(".color").click(function() {
        var data = {color: $(this).text()}
        $.get("/ajax", data, function(data) {
            $("#target").html(`<h1>You selected ${data.turtle}</h1><img src="${data.image}">`)
        });
    });
    $("form").submit(function() {
        var data = $(this).serialize();
        $.get("/ajax", data, function(data) {
            $("#target").html(`<h1>You selected ${data.turtle}</h1><img src="${data.image}">`)
        });
        return false;
    });
});