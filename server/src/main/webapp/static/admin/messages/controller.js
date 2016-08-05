/**
 * Created by Victor on 3/20/2016.
 */
angular.module('hipChatMessagesModule')
    .controller('HipChatMessagesCtrl', ['$scope', '$filter', 'MessagesService',
        function ($scope, $filter, MessagesService) {
        console.log("HipChatMessagesCtrl initialized");
        $scope.messages = [];
        $scope.initializeMotes = function () {
            MessagesService.getMotes().then(function (data) {
                $scope.messages = data;
                console.log("Listing motes!!!! "+$scope.messages);

            }, function (error) {
                console.log("Error loading motes: " + error);
            });

        };

        /*$scope.$watchCollection(function(){return MessagesService.messages;}, function (newValue) {
            console.log("new valuies of motes!" + JSON.stringify(newValue));
        }, true);*/


        $scope.initializeMotes();

    }]);