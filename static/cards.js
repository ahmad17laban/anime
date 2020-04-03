var cards = {
    card1: {
        pic: "/static/img/A.png",
        title: "lorem lorem",
        desc: "helle worldhelle worldhelle worldhelle worldhelle worldhelle worldhelle world",
        date: "1 /4"
    },
    card2: {
        pic: "https://fakeimg.pl/700x250",
        title: "lorme lorme ",
        desc: "helle worldhelle worldhelle worldhelle worldhelle worldhelle world",
        date: "12 / 10"

    },
    card3: {
        pic: "https://fakeimg.pl/700x250",
        title: "lorme",
        desc: "helle worldhelle worldhelle worldhelle worldhelle worldhelle world.",
        date: "24 / 12"
    },
    card4: {
        pic: "https://fakeimg.pl/700x250",
        title: "lorem lorem ",
        desc: "helle worldhelle worldhelle worldhelle worldhelle worldhelle world",
        date: " 12/ 12"
    }

}

$(document).ready(function () {
    for (var key in cards) {
        $("#cardGet").append(
            `<div class="card border-info rounded mb-3  ">
        <img style= "border: solid 1px black;" src=" ${cards[key].pic }" class="card-img-top" alt="..."></img>
        <div class="card-body">
        <h5 class="card-title text-info text-center">${cards[key].title}</h5>
        <p class="card-text text-justify">'+ cards[key].desc + '</p>
        <p class="card-text"><small class="text-muted"> ${cards[key].date} </small></p></div></div>`);
    }
});