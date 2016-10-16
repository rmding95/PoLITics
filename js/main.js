var map;

function initialize() {
  var mapOptions = {
    zoom: 2,
    center: { lat: -33.865427, lng: 151.196123 },
    mapTypeId: 'terrain'
  };

  map = new google.maps.Map(document.getElementById('map'),
    mapOptions);

  // Create a <script> tag and set the USGS URL as the source.
  var script = document.createElement('script');

  // (In this example we use a locally stored copy instead.)
  // script.src = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp';
  script.src = 'https://developers.google.com/maps/documentation/javascript/tutorials/js/earthquake_GeoJSONP.js';
  document.getElementsByTagName('head')[0].appendChild(script);

  map.data.setStyle(function (feature) {
    var magnitude = feature.getProperty('mag');
    return {
      icon: getCircle(magnitude)
      
    };
  });
}

function getCircle(magnitude) {
   if (magnitude >= 4){
  var circle = {
    path: google.maps.SymbolPath.CIRCLE,
    fillColor: 'red',
    fillOpacity: .2,
    scale: Math.pow(2, 3) / 2,
    strokeColor: 'white',
    strokeWeight: .5,
  };
  } else if (magnitude <= 3) {
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
    fillColor: 'green',
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



