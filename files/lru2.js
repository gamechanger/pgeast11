letters = ["A", "B", "C", "D", "E", "F", "G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6"];
buckets = ["A", "B", "C", "D", "E", "F", "G", "H"]
random = false;
on = true;

loaded_blocks = [];

function isLoaded(letter) {
    return loaded_blocks.indexOf(letter) != -1;
}

function loadBlock(letter) {
    var bucket = buckets[Math.floor(letters.indexOf(letter)/4)];
    var bad = ! isLoaded(bucket);
    var style = "background-color:lightgreen;color:black;"
    if ( bad )
        style = "background-color:pink;color:red;font-weight:bold;"
    $("#output").append("<span style='"+style+"'>" + " " + letter + "</span>");
    if ( bad )
        loaded_blocks.splice(0,0,bucket);
    $("#upper").prepend($("#"+bucket));
    for ( var i = 4; i < loaded_blocks.length; i++ ) {
        $("#lower").append($("#"+loaded_blocks[i]));
    }
    loaded_blocks = loaded_blocks.slice(0,4);
}

function loadRandomBlock() {
    loadBlock(letters[Math.floor(Math.random() * letters.length)]);
}

function loadAOrB() {
    loadBlock(letters[Math.floor(Math.random() * 16)]);
}

function iterate() {
    if ( random ) loadRandomBlock();
    else loadAOrB();

    if ( on ) iterateLater();
}

function iterateLater() {
    window.setTimeout("iterate()", 1000 );
}
