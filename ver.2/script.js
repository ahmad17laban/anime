// valid function to check all feilds in sign_up.html
function valid() {
  var name = document.getElementById('inputName3').value
  var email = document.getElementById('inputEmail3').value
  var password = document.getElementById('inputPassword3').value
  var c_password = document.getElementById('inputPassword4').value
  var error_msg = document.getElementById('error_msg')
  var c_box = document.getElementById('gridCheck1')
  var text
  error_msg.style.padding = "10px"
  if (name.length < 5) {
    text = "plese enter valid name"
    error_msg.innerHTML = text
    return false
  }
  // starters needs change 
  if (c_box.checked = false) {
    text = 'please agree on the term of use'
    return false
  }

  if (email.indexOf("@") == -1 || email.length < 10) {
    text = "plese enter valid Email"
    error_msg.innerHTML = text
    return false
  }
  if (password.length < 6) {
    text = "plese enter valid passport"
    error_msg.innerHTML = text
    return false
  }
  if (password != c_password) {
    text = "plese enter valid passport"
    error_msg.innerHTML = text
    return false
  }
  
  if (c_box.checked==false){
    text="please agree on the term of use"
    error_msg.innerHTML = text
    return false


  } 
  // alert('valid')
  return true




}
// JQUERY USE iframe to show the videos in the index.html page 
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
