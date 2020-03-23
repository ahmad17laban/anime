// for fake backend req's ?per_page=10
$(document).ready(function () {
    $("#mybtn").click(function () {
        $.ajax({   
            url: "https://reqres.in/api/users",
            type: 'GET'
        }).done(function (response) {
            var trArr = new Array();
            $.each(response.data, function (i, v) {
                trArr.push('<div class="card mb-3" style="max-width: 540px;">\
                <div class="row no-gutters">\
                  <div class="col-md-4">\
                    <img src="'+v.avatar+'" class="card-img" alt="...">\
                  </div>\
                  <div class="col-md-8">\
                    <div class="card-body">\
                      <h5 class="card-title">'+v.first_name +' ' +v.last_name +'</h5>\
                      <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>\
                      <p class="card-text"><small class="text-muted"></small></p>\
                    </div>\
                  </div>\
                </div>\
              </div>');
            });
            $('#mydata').append(trArr.join('\n'));
        })
    })
});