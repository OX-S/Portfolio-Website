//const log = document.querySelector('.event-log-contents');
//const reload = document.querySelector('#reload');
//
//
//window.addEventListener('load', (event) => {
//    console.log('test');
//});

$(document).ready(function () {
    animate();
});


var id = null;
function animate() {
  var elem = document.getElementById("bg");
  var pos = 0;
  console.log(myBool)
  if (myBool) {
      clearInterval(id);
      id = setInterval(frame, 10);
      function frame() {
        if (pos == 150) {
          elem.remove();
        } else {
          pos++;
          elem.style.top = pos + 'px';
          elem.style.left = pos + 'px';
        }
      }
  }
}
