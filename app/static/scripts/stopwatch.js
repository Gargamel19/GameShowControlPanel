
    function idset(id, string) {
  document.getElementById(id).innerHTML = string;
}

function start_stop() {
const btn = document.getElementById("stopwatch_start_stop")
    if (btn.textContent === "Start") {
        btn.textContent = "Stop";
        stoppuhr.start();
    } else {
        btn.textContent = "Start";
        stoppuhr.stop();
    }
}

var stoppuhr = (function() {
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
      stoppuhr.stop();
      mins = 0;
      secs = 0;
      msecs = 0;
      runden = "";
      anzrunden = 0;
      stoppuhr.html();
    },
    restart: function() {
      stoppuhr.clear();
      stoppuhr.start();
    },
    timer: function() {
      if (stop === 0) {
        msecs++;
        if (msecs === 100) {
          secs ++;
          msecs = 0;
        }
        if (secs === 60) {
          mins++;
          secs = 0;
        }
        stoppuhr.html();
      }
    },
    runde: function() {
      runden = "</td><td>" + mins + "</td><td>" + secs + "</td><td>" + msecs + "</td></tr>" + runden;
      anzrunden++;
      stoppuhr.html();
    },
    set: function(minuten, sekunden, msekunden) {
      stoppuhr.stop();
      mins = minuten;
      secs = sekunden;
      msecs = msekunden;
      runden = "";
      anzrunden = 0;
      stoppuhr.html();
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
setInterval(stoppuhr.timer, 10);