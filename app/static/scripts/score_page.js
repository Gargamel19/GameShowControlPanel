function reload_page(){
    location.reload();
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function readFile() {
    setTimeout(function(){
        sleepFor(1000);
        file = ""
        while (true) {
            xmlHttp = new XMLHttpRequest();
            xmlHttp.open("GET", "http://127.0.0.1:5001/file", false); // false for synchronous request
            xmlHttp.send(null);
            if (file === "") {
                file = xmlHttp.responseText
            } else {
                if (file !== xmlHttp.responseText) {
                    location.reload();
                    break
                }
            }
            console.log("try")
            sleepFor(1000);
        }
    }, 0);
}

function sleepFor(sleepDuration){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){
        /* Do nothing */
    }
}