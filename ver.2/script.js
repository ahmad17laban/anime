function valid(){
    var name = document.getElementById('inputName3').value
    var email = document.getElementById('inputEmail3').value
    var password = document.getElementById('inputPassword3').value
    var c_password = document.getElementById('inputPassword4').value
    var error_msg= document.getElementById('error_msg')
    var text  
    error_msg.style.padding= "10px"
    if (name.length < 5){
      text="plese enter valid name"
      error_msg.innerHTML= text
      return false
    }
    
    if ( email.indexOf("@") == -1 ||name.length < 10){
      text="plese enter valid Email"
      error_msg.innerHTML= text
      return false
    }
    if (password.length < 6 ){
      text="plese enter valid passport"
      error_msg.innerHTML= text
      return false
    }
    if (password != c_password ){
      text="plese enter valid passport"
      error_msg.innerHTML= text
      return false
    }
    alert('valid')
    return true 




}
$('#modal1').on('hidden.bs.modal', function (e) {
  // do something...
  $('#modal1 iframe').attr("src", $("#modal1 iframe").attr("src"));
});

$('#modal6').on('hidden.bs.modal', function (e) {
  // do something...
  $('#modal6 iframe').attr("src", $("#modal6 iframe").attr("src"));
});

$('#modal4').on('hidden.bs.modal', function (e) {
  // do something...
  $('#modal4 iframe').attr("src", $("#modal4 iframe").attr("src"));
});
