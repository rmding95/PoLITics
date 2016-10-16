var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function($routeProvider, $locationProvider, $httpProvider) {

  $httpProvider.defaults.useXDomain = true;
  delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

myApp.controller("main", function($scope, $http) {
  $scope.clickMe = function() {
      $http({
        method: 'GET',
        url: 'http://http://127.0.0.1:5000/data'
      })
      .success(function(data) {
        console.log(data)
      });
  }
});