function init_map() {
    var myOptions = {
        zoom: 4,
        center: new google.maps.LatLng(42.228517539011186, -96.15234412500001),
        mapTypeId: google.maps.MapTypeId.TERRAIN
    };
    map = new google.maps.Map(document.getElementById('gmap_canvas'),
        myOptions);
  
    infowindow = new google.maps.InfoWindow({
        content: '<strong>Title<\/strong><br>United Sates<br>'
    });
    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map, marker);
    });
    infowindow.open(map, marker);
}
google.maps.event.addDomListener(window, 'load', init_map);