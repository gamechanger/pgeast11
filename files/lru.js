letters = ["A", "B", "C", "D", "E", "F", "G", "H"];
random = false;
on = true;

loaded_blocks = [];

function isLoaded(letter) {
    return loaded_blocks.indexOf(letter) != -1;
}

function loadBlock(letter) {
    var bad = ! isLoaded(letter);
    var style = "background-color:lightgreen;color:black;"
    if ( bad )
        style = "background-color:pink;color:red;font-weight:bold;"
    $("#output").append("<span style='"+style+"'>" + " " + letter + "</span>");
    if ( bad )
        loaded_blocks.splice(0,0,letter);
    $("#upper").prepend($("#"+letter));
    for ( var i = 4; i < loaded_blocks.length; i++ ) {
        $("#lower").append($("#"+loaded_blocks[i]));
    }
    loaded_blocks = loaded_blocks.slice(0,4);
}

function loadRandomBlock() {
    loadBlock(letters[Math.floor(Math.random() * letters.length)]);
}

function loadAOrB() {
    loadBlock(letters[Math.floor(Math.random() * 4)]);
}

function iterate() {
    if ( random ) loadRandomBlock();
    else loadAOrB();

    if ( on ) iterateLater();
}

function iterateLater() {
    window.setTimeout("iterate()", 1000 );
}
