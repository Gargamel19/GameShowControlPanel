
file = ""
while (true){
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "http://127.0.0.1:5001/file", false ); // false for synchronous request
    xmlHttp.send( null );
    if(file === ""){
        file = xmlHttp.responseText
    }else{
        if(file !== xmlHttp.responseText){
            location.reload();
        }
    }
    var start = new Date().getTime();
    while (new Date().getTime() < start + 1000);
}

