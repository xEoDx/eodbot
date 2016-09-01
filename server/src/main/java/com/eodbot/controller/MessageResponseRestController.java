package com.eodbot.controller;

import com.eodbot.model.ErrorMessage;
import com.eodbot.model.MessageMapDictionary;
import com.eodbot.service.MessageResponseService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Created by Victor on 18/07/2016.
 */
@RestController
public class MessageResponseRestController {
    private static final Logger LOGGER = LoggerFactory.getLogger(MessageResponseRestController.class);
    @Autowired
    private MessageResponseService messageResponseService;

    @RequestMapping(value = "/message", method = RequestMethod.GET)
    public ResponseEntity listAll() {
        LOGGER.info("Listing all messages");
        List<MessageMapDictionary> messageMapDictionaries = messageResponseService.findAll();
        if (messageMapDictionaries.isEmpty()) {
            return new ResponseEntity<>(new ErrorMessage("No messages were found"), HttpStatus.NO_CONTENT);
        }
        return new ResponseEntity<>(messageMapDictionaries, HttpStatus.OK);
    }

    @RequestMapping(value = "/message", method = RequestMethod.POST)
    public ResponseEntity save(@RequestBody MessageMapDictionary messageMapDictionary) {
        LOGGER.info("Creating MessageMapDictionary: {}", messageMapDictionary);

        if (messageResponseService.findAll().stream().filter(m -> m.getKey().equals(messageMapDictionary.getKey())).count() > 0) {
            return new ResponseEntity<>(new ErrorMessage("Already existing message key " + messageMapDictionary.getKey()), HttpStatus.BAD_REQUEST);
        }

        messageResponseService.save(messageMapDictionary);

        return listAll();
    }

    @RequestMapping(value = "/message", method = RequestMethod.PUT)
    public ResponseEntity update(@RequestBody MessageMapDictionary messageMapDictionary) {
        LOGGER.info("Updating MessageMapDictionary: {}", messageMapDictionary);

        messageResponseService.save(messageMapDictionary);

        return listAll();
    }

    @RequestMapping(value = "/message/{id}", method = RequestMethod.DELETE)
    public ResponseEntity delete(@PathVariable Long id) {
        LOGGER.info("Deleting MessageMapDictionary ID: {}", id);

        messageResponseService.remove(id);

        return listAll();
    }
}
