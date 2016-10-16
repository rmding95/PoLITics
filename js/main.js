var map;

function initialize() {
  var mapOptions = {
    zoom: 4,
    center: { lat: 39.8282, lng: -98.5795 },
    mapTypeId: 'terrain'
  };

  map = new google.maps.Map(document.getElementById('map'),
    mapOptions);

  // Create a <script> tag and set the USGS URL as the source.
  //var script = document.createElement('script');

  // (In this example we use a locally stored copy instead.)
  // script.src = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp';
  
  
  $.ajax({
    url: "127.0.0.1:5000/data",
    type: "GET",
    contentType: 'application/json; charset=utf-8',
    success: function(data){
      console.log(data);
      plotData(data)
    }, 
    error: function(data){
      console.log(data)
    }
  }), 



  function plotData (data){
  
  // script.src = 'https://developers.google.com/maps/documentation/javascript/tutorials/js/earthquake_GeoJSONP.js';
  document.getElementsByTagName('head')[0].appendChild(script);

  map.data.setStyle(function (feature) {
    var color = feature.getProperty('party');
    return {
      icon: getCircle(color)
      
    };
  });
}

function getCircle(color) {
   if (color == Democrat){
  var circle = {
    path: google.maps.SymbolPath.CIRCLE,
    fillColor: 'blue',
    fillOpacity: .2,
    scale: Math.pow(2, 3) / 2,
    strokeColor: 'white',
    strokeWeight: .5,
  };
  } else {
    var circle = {
    path: google.maps.SymbolPath.CIRCLE,
    fillColor: 'red',
    fillOpacity: .2,
    scale: Math.pow(2, 3) / 2,
    strokeColor: 'white',
    strokeWeight: .5,
  };
  }

  return circle;
}

function eqfeed_callback(results) {
  map.data.addGeoJson(results);

  setTimeout(eqfeed_callback(null, results), 2000); 
}

}

//myCircle.transition()
//  .delay(600)
//  circle.exit().remove
