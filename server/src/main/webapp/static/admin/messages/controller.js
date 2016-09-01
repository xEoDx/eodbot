/**
 * Created by Victor on 3/20/2016.
 */
angular.module('hipChatMessagesModule')
    .controller('HipChatMessagesCtrl', ['$scope', '$log','$filter', '$uibModal', 'MessagesService', 'NgTableParams',
        function ($scope, $log, $filter, $uibModal, MessagesService, NgTableParams) {
            $log.info("HipChatMessagesCtrl initialized");
            $scope.showAlert = false;
            $scope.alertMessage = "";

            $scope.initializeMotes = function () {
                MessagesService.list().then(function (data) {
                    updateTable(data);
                    $log.log("Listing messages:  ", data);

                }, function (error) {
                    $log.warn("Error loading messages: ", error);
                    setAlertStatus("danger", error.data.message);
                });

            };

            $scope.delete = function (message) {
                MessagesService.remove(message.id).then(function (response) {
                    updateTable(response);
                    setAlertStatus("success", "Message id "+message.id+" has been deleted!");
                }, function(error){
                    setAlertStatus("danger", error.data.message);

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
                    $log.log("Updating item ",updatedItem);
                    if(updatedItem.id == 0) {
                        MessagesService.save(updatedItem).then(function (response) {
                            $log.log("Done! Response is: ", response);
                            updateTable(response);
                            setAlertStatus("success", "Message id "+updatedItem.id+" has been updated!");
                        }, function(error){
                            setAlertStatus("danger", error.data.message);
                        });
                    } else {
                        MessagesService.update(updatedItem).then(function (response) {
                            $log.log("Done! Response is: ", response);
                            updateTable(response);
                            setAlertStatus("success", "Message id "+updatedItem.id+" has been updated!");
                        }, function(error){
                            setAlertStatus("danger", error.data.message);
                        });
                    }

                }, function () {
                    $log.log('Modal dismissed at: ' + new Date());
                });
            };


            function updateTable(data){
                $scope.tableParams.reload().then(function(r) {
                    if (data.length === 0 && $scope.tableParams.total() > 0) {
                        $scope.tableParams.page($scope.tableParams.page() - 1);
                        $scope.tableParams.reload();
                    }
                });
            }


            $scope.tableParams = new NgTableParams({
                page: 1,            // show first page
                count: 10           // count per page
            }, {
                getData: function(params) {
                    // ajax request to api
                    return MessagesService.list().then(function(data) {
                        var orderedData = params.sorting() ?
                            $filter('orderBy')(data, params.orderBy()) : $scope.items;

                        params.total(orderedData.length); // set total for recalc pagination

                        orderedData = params.filter() ?
                            $filter('filter')(orderedData, params.filter()) : orderedData;

                        orderedData = orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count());

                        return orderedData;
                    });
                }
            });


            $scope.hideAlert = function() {
                $scope.showAlert = false;
            };

            function setAlertStatus(alertType, text){
                $scope.showAlert = true;
                $scope.alertType = "alert-"+alertType;
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