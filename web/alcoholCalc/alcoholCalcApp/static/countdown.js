window.onload = function() {
  var hour = 2;
  var sec = 60;
  setInterval(function() {
    document.getElementById("timer").innerHTML = hour + " : " + sec;
    sec--;
    if (sec == 00) {
      hour--;
      sec = 60;
      if (hour == 0) {
        hour = 2;
      }
    }
  }, 1000);
}
