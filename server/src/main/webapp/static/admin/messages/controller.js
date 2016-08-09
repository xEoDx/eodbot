/**
 * Created by Victor on 3/20/2016.
 */
angular.module('hipChatMessagesModule')
    .controller('HipChatMessagesCtrl', ['$scope', '$log','$filter', '$uibModal', 'MessagesService',
        function ($scope, $log, $filter, $uibModal, MessagesService) {
            $log.info("HipChatMessagesCtrl initialized");
            $scope.showAlert = false;
            $scope.alertMessage = "";

            $scope.messages = [];
            $scope.initializeMotes = function () {
                MessagesService.list().then(function (data) {
                    $scope.messages = data;
                    $log.log("Listing messages:  ", $scope.messages);

                }, function (error) {
                    $log.warn("Error loading messages: ", error);
                    setAlertStatus("error", "Error on listing messages!");
                });

            };

            $scope.delete = function (message) {
                MessagesService.remove(message.id).then(function (response) {
                    $scope.messages = response;
                    setAlertStatus("success", "Message id "+message.id+" has been deleted!");
                }, function(error){
                    setAlertStatus("error", "Error when deleting message "+message.id);

                });
            };

            $scope.open = function (message) {
                var modalInstance = $uibModal.open({
                    templateUrl: 'messagesModal.html',
                    controller: 'MessagesModalCtrl',
                    resolve: {
                        message: function () {
                            return message;
                        }
                    }
                });

                modalInstance.result.then(function (updatedItem) {
                    MessagesService.update(updatedItem).then(function (response) {
                        $log.log("Done! Response is: ", response);
                        $scope.messages = response;
                        setAlertStatus("success", "Message id "+updatedItem.id+" has been updated!");
                    }, function(error){
                        setAlertStatus("error", "Error on updating message id "+updatedItem.id);

                    });

                }, function () {
                    $log.log('Modal dismissed at: ' + new Date());
                });
            };


            $scope.hideAlert = function() {
                $scope.showAlert = false;
            };

            function setAlertStatus(alertType, text){
                $scope.showAlert = true;
                $scope.alertType = alertType;
                $scope.alertMessage = text;
            }

            $scope.initializeMotes();

        }])
    .controller('MessagesModalCtrl', ['$scope', '$log', '$uibModalInstance', 'message', function ($scope, $log, $uibModalInstance, message) {
        $log.log("Initializing messages modal ctrl");
        $scope.message = message;
        if (message == undefined) {
            $scope.message = {
                id: 0,
                key: '',
                responses: [{text: ""}]
            }
        }


        $scope.ok = function () {
            $scope.message = parseMessageAnswer($scope.message);
            $uibModalInstance.close($scope.message);

        };

        $scope.cancel = function () {
            $uibModalInstance.dismiss('cancel');
        };

        $scope.addAnswer = function () {
            $scope.message.responses.push({text: ""});
        };

        $scope.removeAnswer = function (index) {
            $scope.message.responses.splice(index, 1);
        };

        function parseMessageAnswer(message) {
            var msg = {};
            var responses = [];

            msg.id = message.id;
            msg.key = message.key;
            message.responses.forEach(function (response) {
                responses.push(response.text);
            });
            msg.responses = responses;

            return msg;
        }
    }]);