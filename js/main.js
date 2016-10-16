var map;

function initialize() {
  var map = new google.maps.Map(d3.select("#map").node(), {
    zoom: 4,
    center: new google.maps.LatLng(39.8282, -98.5795),
    mapTypeId: google.maps.MapTypeId.TERRAIN
  });

   $.ajax({
    url: "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp",
    type: "GET",
    contentType: 'application/json; charset=utf-8',
    success: function(data){
      console.log(data);
      plotData(data)
    }, 
    error: function(data){
      console.log(data)
    }
  })

  function plotData(data){

  var overlay = new google.maps.OverlayView();

  // Add the container when the overlay is added to the map.
  overlay.onAdd = function() {
    var layer = d3.select(this.getPanes().overlayLayer).append("div")
        .attr("class", "stations");

    // Draw each marker as a separate SVG element.
    // We could use a single SVG, but what size would it have?
    overlay.draw = function() {
      var projection = this.getProjection(),
          padding = 10;

      var marker = layer.selectAll("svg")
          .data(d3.entries(data))
          .each(transform) // update existing markers
        .enter().append("svg")
          .each(transform)
          .attr("class", "marker");

      // Add a circle.
      marker.append("circle")
          .attr("r", 4.5)
          .attr("cx", padding)
          .attr("cy", padding);

      // Add a label.
      marker.append("text")
          .attr("x", padding + 7)
          .attr("y", padding)
          .attr("dy", ".31em")
          .text(function(d) { return d.key; });

      function transform(d) {
        d = new google.maps.LatLng(d.value[1], d.value[0]);
        d = projection.fromLatLngToDivPixel(d);
        return d3.select(this)
            .style("left", (d.x - padding) + "px")
            .style("top", (d.y - padding) + "px");
      }
    };
  };

  // Bind our overlay to the map…
  overlay.setMap(map);
}}
