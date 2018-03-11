$(document).ready(function() {
    $(".action").submit(function(e) {
        e.preventDefault();
        var data = $(this).serialize();
        $.post("/", data, function(data) {
            setGold(data);
            updateActivity(data);
        });
    });
});

function setGold(data) {
    var score = Number($("#score").text());
    if (data["win"]) {
        score += Number(data["gold"]);
    }
    else {
        score -= Number(data["gold"]);
    }
    $("#score").text(score);
}

function updateActivity(data) {
    if (data["win"]) {
        var result = "won"
        var result2 = "noice!"
    }
    else {
        var result = "lost"
        var result2 = "ouch!"
    }
    var str = `<li>You went to the ${data["activity"]} and ${result} ${data["gold"]} gold -- ${result2}</li>`
    $("#activities ul").append(str);
}