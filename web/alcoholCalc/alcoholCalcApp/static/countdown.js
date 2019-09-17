window.onload
function timer(h) {
  var hour = h;
  var sec = h;
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

output = document.getElementById("output");
console.log(output);

if (output != "") {
  timer(text);
}
