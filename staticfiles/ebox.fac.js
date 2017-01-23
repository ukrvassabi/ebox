(function() {
	
	"use strict";

	angular
		.module("ebox")
		.factory("EboxService", function($http) {
			return {
				getUser: function() {
					return $http.get("/api/v1/get-user/");
				},
				logout: function() {
					return $http.get("/api/v1/logout/");
				},
				getMails: function() {
					return $http.get("/api/v1/get-mails/");
				}
			}
		});
})();