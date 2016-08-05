/**
 * Created by Victor on 3/27/2016.
 */
angular.module('hipChatMessagesModule')
    .factory('MessagesService', ['$http', '$q', function ($http, $q) {
        console.log("MessagesService initialized");
        var messages = [];

        return {
            getMotes: function () {
                return $http({
                    method: 'GET',
                    url: '/message'
                }).then(function successCallback(response) {
                    this.messages = response.data;
                    console.log("Updating messages on the service");
                    return response.data;
                }, function errorCallback(response) {
                    return $q.reject(response);
                });
            },
            update: function (message) {
                return $http({
                    method: 'POST',
                    url: '/message',
                    data: message
                }).then(function successCallback(response) {
                    return response.data;
                }, function errorCallback(response) {
                    return $q.reject(response);
                });
            },
            messages: messages
        }
    }]);