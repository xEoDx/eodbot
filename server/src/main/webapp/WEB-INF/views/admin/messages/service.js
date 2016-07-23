/**
 * Created by Victor on 3/27/2016.
 */
angular.module('hipchatMessagesModule')
    .factory('MessagesService', ['$http', '$q', function ($http, $q) {
        console.log("MessagesService initialized");
        var messages = [];

        return {
            getMotes: function () {
                return $http({
                    method: 'GET',
                    url: '/rest/message/get'
                }).then(function successCallback(response) {
                    this.messages = response.data;
                    console.log("Updating messages on the servicve");
                    return response.data;
                }, function errorCallback(response) {
                    return $q.reject(response);
                });
            },
            update: function (mote) {
                return $http({
                    method: 'POST',
                    url: '/rest/message/update/',
                    data: mote
                }).then(function successCallback(response) {
                    return response.data;
                }, function errorCallback(response) {
                    return $q.reject(response);
                });
            },
            messages: messages
        }
    }]);