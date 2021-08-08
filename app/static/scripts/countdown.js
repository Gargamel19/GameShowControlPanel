
    function idset(id, string) {
  document.getElementById(id).innerHTML = string;
}

function start_stop() {
const btn = document.getElementById("countdown_start_stop")
    if (btn.textContent === "Start") {
        countdown.start();
        btn.textContent = "Stop";
    } else {
        btn.textContent = "Start";
        countdown.stop();
    }
}

var countdown = (function() {
  var stop = 1;
  var mins = 0;
  var secs = 0;
  var msecs = 0;
  var runden = "";
  var anzrunden = 0;
  return {
    start: function() {
      stop = 0;
    },
    stop: function() {
      stop = 1;
    },
    clear: function() {
      countdown.stop();
      mins = document.getElementById("countdown_min").value;
      secs = document.getElementById("countdown_sec").value;
      msecs = 0;
      runden = "";
      anzrunden = 0;
      countdown.html();
    },
    restart: function() {
      countdown.clear();
      countdown.start();
    },



    timer: function() {
      if (stop === 0) {
        msecs--;
        if (msecs === -1) {
          secs --;
          msecs = 99;
        }
        if (secs === -1) {
          mins--;
          secs = 59;
        }
        countdown.html();
      }
    },
    runde: function() {
      runden = "</td><td>" + mins + "</td><td>" + secs + "</td><td>" + msecs + "</td></tr>" + runden;
      anzrunden++;
      countdown.html();
    },
    set: function(minuten, sekunden, msekunden) {
      countdown.stop();
      mins = minuten;
      secs = sekunden;
      msecs = msekunden;
      runden = "";
      anzrunden = 0;
      countdown.html();
    },
    html: function() {
      idset("minuten", ("00" + mins).slice(-2));
      idset("sekunden", ("00" + secs).slice(-2));
      idset("msekunden", ("00" + msecs).slice(-2));
      idset("runden", runden);
      idset("anzrunden", anzrunden + " Runden");
    }
  }
})();
setInterval(countdown.timer, 10);