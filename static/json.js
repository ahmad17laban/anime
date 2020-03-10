var cards = {
    card1: {
        pic: "/Img/A.png",
        title: "TAttack on Titan: The True Origin of The Founding Titan, Ymir, Revealed",
        
    },
    card2: {
        pic: "/Img/B.jpg",
        title: "TAttack on Titan: The True Origin of The Founding Titan, Ymir, Revealed",
        
    },card3: {
        pic: "/Img/c.jpg",
        title: "TAttack on Titan: The True Origin of The Founding Titan, Ymir, Revealed",
        
    },
}


function cardPrint(container) {

    for (var key in cards) {
        var card = '<div class="card card-body mb-3">\
        <div class="media d-block d-md-flex">\
          <div class="media-body pr-md-3 pr-0 text-center text-md-left">\
            <p>\
              <h4>'
              card+= cards[key].title+'</h4>\
              </p>\
              <button type="button" class="btn btn-primary btn-md">Read more</button>\
            </div>\
            <img class="d-flex mr-3 avatar-2 mt-md-0 mt-3 mx-auto"\
              src="'+cards[key].pic+'" alt="Generic placeholder image">\
              </div>\
            </div>'
        document.getElementById(container).innerHTML += card;
        console.log("loops")
    }


}