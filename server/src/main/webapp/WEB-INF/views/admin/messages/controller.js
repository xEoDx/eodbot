/**
 * Created by Victor on 3/20/2016.
 */
angular.module('hipchatMessagesModule')
    .controller('HipChatMessagesCtrl', ['$scope', '$filter', 'MessagesServices', function ($scope, $filter, MessagesService) {
        console.log("HipChatMessagesCtrl initialized");

        var initializeMotes = function () {
            MessagesService.getMotes().then(function (data) {
                $scope.messages = data;
                console.log("Listing motes!!!! "+$scope.messages);
                console.log("Listing motes2!!!! "+MessagesService.messages);

            }, function (error) {
                console.log("Error loading motes: " + error);
            });

        };

        $scope.$watchCollection(function(){return MessagesService.messages;}, function (newValue) {
            console.log("new valuies of motes!" + JSON.stringify(newValue));
        }, true);


        initializeMotes();

    }]);