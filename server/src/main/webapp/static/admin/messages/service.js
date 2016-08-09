/**
 * Created by Victor on 3/27/2016.
 */
angular.module('hipChatMessagesModule')
    .factory('MessagesService', ['$http', '$q', '$log', function ($http, $q, $log) {
        $log.info("MessagesService initialized");
        function parseMessages(response) {
            var messages = [];
            response.data.forEach(function (message) {
                var responses = [];
                message.responses.forEach(function (response) {
                    responses.push({text: response});
                });
                messages.push({
                    id: message.id,
                    key: message.key,
                    responses: responses
                });
            });
            return messages;
        }

        return {
            list: function () {
                return $http({
                    method: 'GET',
                    url: '/message'
                }).then(function successCallback(response) {
                    return parseMessages(response);
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
                    $log.info("Message ",message," has been updated");
                    return parseMessages(response);
                }, function errorCallback(response) {
                    $log.error("Error on updating message ",message);
                    return $q.reject(response);
                });
            },
            remove: function (id) {
                return $http({
                    method: 'DELETE',
                    url: '/message/'+id
                }).then(function successCallback(response){
                    $log.info("Message ID ",id," has been deleted");
                    return parseMessages(response);
                }, function errorCallback(response) {
                    $log.error("Error on removing message ID ",id);
                    return $q.reject(response);
                });
            }
        }
    }]);