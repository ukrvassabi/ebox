(function() {
	
	"use strict";

	angular
		.module("ebox")
		.controller("LoginController", function($state, EboxService) {
			EboxService.getUser().then(function(response) {
				$state.go("ebox");
			}, function() {
				console.log("User is not authenticated");
			});
		})
		.controller("EboxController", function($rootScope, $state, EboxService) {
			var vm = this;

			$rootScope.$broadcast("blockSpinner:show");

			EboxService.getUser().then(function(response) {
				vm.user = response.data.user;

				EboxService.getMails().then(function(response) {
					vm.emails = response.data;
					$rootScope.$broadcast("blockSpinner:hide");
				})
			}, logout);

			vm.logout = function() {
				EboxService.logout().then(logout);
			}

			function logout() {
				$state.go("home");
			}
		});
})();