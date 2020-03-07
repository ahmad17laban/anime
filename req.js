$(document).ready(function () {
$("#mybtn").click(function  ()  { 
    $.ajax({
        url: "https://reqres.in/api/users?per_page=10",
        data: {},
        type:'GET'
        // beforeSend: function(){}
    }).done(function(response) {
        var trArr = new Array();

        $.each(response.data, function(i, v){
            trArr.push('<tr><td>' + v.id + '</td><td>' + v.first_name + '</td><td>' + v.last_name + '</td><td><img src="' + v.avatar + '" width="120px" /></td></tr>');
        });
        $('table#alk-table tbody').append(trArr.join('\n'));
    })  } ) } ) ;