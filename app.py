import os.path
import pymongo
from pymongo.errors import AutoReconnect
#host = "AirKiril.local"
host = "iMac27.local"
conn = pymongo.Connection('mongodb://%s:30000,%s:30001' % (host,host))
#conn = pymongo.Connection('mongodb://AirKiril.local:40000')


import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return """
<a href="/simple">OMG WOW</a>
<div style="width:400px; margin:0px auto 0px auto; text-align: center; border: thin solid #ccc; background-color: #eee;">
<h1>Scaling from Toys to Traffic</h1>
Kiril Savino, @kirilnyc
<br/>
CTO, GameChanger Media, Inc.
<br/>
<b>www.GameChanger.io</b>
<br/>
&raquo; jobs@gc.io &laquo;
<br/>
"slides": http://github.com/kiril/pgeast11
</div>
"""

    @cherrypy.expose
    def simple(self):
        return """
<a href="/lru">LRU</a>
<div style="width:400px; margin: 0px auto 0px auto; padding: 20px; border: thin solid #ccc; background-color: #eee; font-family:mono;">
<pre>
team = {"name": "NYC Jaguars", "sport": "baseball"}
mongo.datadb.team.save(team) # omg wow
</pre>
<br/>
</div>
        """

    @cherrypy.expose
    def lru(self):
        return """
<script src="jquery-1.4.2.min.js"></script>
<script src="lru.js"></script>
<style>
.container { background-color: #eee; border: thin solid #ccc; height: 35px; padding: 10px; width: 250px; margin: 0px auto 0px auto; }
#lower { height: 55px; }
.block { height: 15px; padding: 5px; border: thin solid #ccc; text-align: center; width: 50px; float: left; }
#a { background-color: pink; }
#b { background-color: lightblue; }
#c { background-color: lightgreen; }
#d { background-color: orange; }
#e { background-color: red; color: white; }
#f { background-color: darkgreen; color: white; }
#g { background-color: yellow; }
#h { background-color: purple; color: white; }
#output { margin: 10px auto 0px auto; width: 250px; }
#controls { margin: 0px auto 0px auto; width: 250px; text-align: center; }
</style>
<a href="/lru2">MOAR</a>
<div id="upper" class="container">
</div>
<div id="lower" class="container">
<div id="A" class="block">A</div>
<div id="B" class="block">B</div>
<div id="C" class="block">C</div>
<div id="D" class="block">D</div>
<div id="E" class="block">E</div>
<div id="F" class="block">F</div>
<div id="G" class="block">G</div>
<div id="H" class="block">H</div>
</div>
<div id="controls">
<a href="javascript:iterateLater()">Start</a> | <a href="javascript:window.random=false;">Nice</a> | <a href="javascript:window.random=true;">Not Nice</a>
</div>
<div id="output"></div>
"""

    @cherrypy.expose
    def lru2(self):
        return """
<script src="jquery-1.4.2.min.js"></script>
<script src="lru2.js"></script>
<style>
.container { background-color: #eee; border: thin solid #ccc; height: 35px; padding: 10px; width: 250px; margin: 0px auto 0px auto; }
#lower { height: 55px; }
.block { height: 15px; padding: 5px; border: thin solid #ccc; text-align: center; width: 50px; float: left; }
#A { background-color: pink; }
#B { background-color: lightblue; }
#C { background-color: lightgreen; }
#D { background-color: orange; }
#E { background-color: red; color: white; }
#F { background-color: darkgreen; color: white; }
#G { background-color: yellow; }
#H { background-color: purple; color: white; }
#output { margin: 10px auto 0px auto; width: 250px; }
#controls { margin: 0px auto 0px auto; width: 250px; text-align: center; }
</style>
<a href="/users">Growing Up</a>
<div id="upper" class="container">
</div>
<div id="lower" class="container">
<div id="A" class="block">ABCD</div>
<div id="B" class="block">EFGH</div>
<div id="C" class="block">IJKL</div>
<div id="D" class="block">MNOP</div>
<div id="E" class="block">QRST</div>
<div id="F" class="block">UVWX</div>
<div id="G" class="block">YZ12</div>
<div id="H" class="block">3456</div>
</div>
<div id="controls">
<a href="javascript:iterateLater()">Start</a> | <a href="javascript:window.random=false;">Nice</a> | <a href="javascript:window.random=true;">Not Nice</a>
</div>
<div id="output"></div>
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
<a href="javascript:startPolling();">start</a> |
<a href="javascript:stopPolling();">stop</a>
<br/>
<a href="/">Okay then</a>
        """

    @cherrypy.expose
    def poll(self):
        while True:
            try:
                return "%s" % conn.data.thingoes.find({'x': True}).count()
            except AutoReconnect:
                continue
            except:
                break

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print current_dir
    conf = {'/': {'tools.staticdir.on': True,
                  'tools.staticdir.dir': current_dir + '/files'},
            }
    cherrypy.quickstart(Root(), "/", config=conf)
