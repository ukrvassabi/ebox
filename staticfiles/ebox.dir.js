(function() {

	"use strict";

	angular
		.module("ebox")
		.directive("eboxSpinner", function($rootScope) {
		    return {
		      restrict: "E",
		      replace: true,
		      template: "<div class='spinner-bg' ng-show='showSpinner'>" +
		                  "<div class='spinner'>Loading...</div>" +
		                "</div>",
		      link: function (scope) {
		        $rootScope.$on("blockSpinner:show", function() {
		          scope.showSpinner = true;
		        });
		        $rootScope.$on("blockSpinner:hide", function() {
		          scope.showSpinner = false;
		        });
		      }
		    }
		  });
})();
