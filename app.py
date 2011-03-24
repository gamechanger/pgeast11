import os.path
import pymongo
conn = pymongo.Connection('mongodb://AirKiril.local:30000,AirKiril.local:30001')


import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return ""

    @cherrypy.expose
    def lru(self):
        return """
<script src="jquery-1.4.2.min.js"></script>
<style>
.container { background-color: #eee; border: thin solid #ccc; height: 35px; padding: 10px; width: 250px; margin: 0px auto 0px auto; }
.block { height: 15px; padding: 5px; border: thin solid #ccc; text-align: center; width: 50px; float: left; }
#a { background-color: pink; }
#b { background-color: lightblue; }
#c { background-color: lightgreen; }
#d { background-color: orange; }
</style>
<div id="upper" class="container">
</div>
<div id="lower" class="container">
<div id="a" class="block">A</div>
<div id="b" class="block">B</div>
<div id="c" class="block">C</div>
<div id="d" class="block">D</div>
</div>
<script>
</script>
"""

    @cherrypy.expose
    def users(self):
        return """
<script src="jquery-1.4.2.min.js"></script>
<img width="100" height="100" src="smile.png" id="smile" style="display:none;"/>
<img width="100" height="100" src="frown.png" id="frown" style="display:none;"/>
<img width="100" height="100" src="dead.png" id="dead" style="display:none;"/>
<table>
<tr><td>Response:</td><td id="rescode">-</td></tr>
<tr><td>Time:</td><td id="time">-</td></tr>
<tr><td>Count:</td><td id="result"></td></tr>
</table>
<script>
$("#smile").show()
function smile() {
  $("#frown").hide();
  $("#dead").hide();
  $("#smile").show();
}
function frown() {
  $("#dead").hide();
  $("#smile").hide();
  $("#frown").show();
}
function die() {
  $("#smile").hide();
  $("#frown").hide();
  $("#dead").show();
}
function getDataSoon() {
  if ( on )
    window.setTimeout("getData()", 1000);
}
var startReq = 0;
var gotData = 0
var on = false;
function maybeFrown() {
  if ( startReq > gotData && new Date().getTime() - gotData > 200 )
    frown();
}
function returned(rescode) {
  gotData = new Date().getTime();
  var took = gotData - startReq;
  $("#time").html( (took > 1000 ? took / 1000.0 + "s" : took + "ms" ) );
  $("#rescode").html(rescode);
}
function getData() {
  startReq = new Date().getTime();
  window.setTimeout("maybeFrown()", 210);
  
  $.ajax({success:
          function(data, textStatus, xhr) {
            returned(textStatus);
            try {
              var num = parseInt(data);
              if ( num < 0 ) { alert("couldn't parse " + data ); throw "oh no"; }
              $("#result").html(num + " thingoes with {x=true}");
              if ( gotData - startReq > 200 ) { frown(); }
              else { smile(); }
            } catch ( e ) { die(); }

            getDataSoon();
          },
          error:
          function(xhr, textStatus, error) {
            returned(textStatus);
            die();
            getDataSoon();
          },
          url: "/poll",
          });
}
function startPolling() {
  on = true;
  getDataSoon();
}

function stopPolling() {
  on = false;
}
</script>
<a href="javascript:startPolling();">start</a>
<a href="javascript:stopPolling();">stop</a>
        """

    @cherrypy.expose
    def poll(self):
        return "%s" % conn.data.thingoes.find({'x': True}).count()

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print current_dir
    conf = {'/': {'tools.staticdir.on': True,
                  'tools.staticdir.dir': current_dir + '/files'},
            }
    cherrypy.quickstart(Root(), "/", config=conf)
