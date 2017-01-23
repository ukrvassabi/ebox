(function () {
	
	"use strict";

	angular
		.module("ebox", ["ui.router"])
		.config(function($stateProvider, $urlRouterProvider) {

			$urlRouterProvider.otherwise("/");

			$stateProvider
			  .state("home", {
			    url: "/",
			    templateUrl: "static/login.tpl.html",
			    controller: "LoginController",
			    controllerAs: "login"
			  })
			  .state("ebox", {
			    url: "/ebox",
			    templateUrl: "static/ebox.tpl.html",
			    controller: "EboxController",
			    controllerAs: "ebox"
			  });
		});
})();
