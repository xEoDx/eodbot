/**
 * Created by Victor on 3/20/2016.
 */
angular.module('routingModule', ['ngRoute'])
    .config(["$routeProvider", "$locationProvider", function($routeProvider, $locationProvider)
    {
        console.log("Initializing routeProvider");
       /* $locationProvider.html5Mode({
            enabled: true
        });*/
        $routeProvider
            .when('/', {
                templateUrl: 'static/admin/messages/messages.html',
                controller: 'HipChatMessagesCtrl'
            })
            .when('/messages', {
                templateUrl: 'static/admin/messages/messages.html',
                controller: 'HipChatMessagesCtrl'
            })
            .otherwise({
                redirectTo : '/'
            });
    }]);