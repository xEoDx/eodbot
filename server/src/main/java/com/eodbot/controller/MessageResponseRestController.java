package com.eodbot.controller;

import com.eodbot.model.MessageMapDictionary;
import com.eodbot.service.MessageResponseService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.util.UriComponentsBuilder;

import java.util.List;

/**
 * Created by Victor on 18/07/2016.
 */
@RestController
public class MessageResponseRestController {
    private static final Logger LOGGER = LoggerFactory.getLogger(MessageResponseRestController.class);
    @Autowired
    MessageResponseService messageResponseService;

    @RequestMapping(value = "/message/", method = RequestMethod.GET)
    public ResponseEntity<List<MessageMapDictionary>> listAll() {
        List<MessageMapDictionary> messageMapDictionaries = messageResponseService.findAll();
        if(messageMapDictionaries.isEmpty()){
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);//You many decide to return HttpStatus.NOT_FOUND
        }
        return new ResponseEntity<>(messageMapDictionaries, HttpStatus.OK);
    }

    @RequestMapping(value = "/message/", method = RequestMethod.POST)
    public ResponseEntity<Void> createUser(@RequestBody MessageMapDictionary messageMapDictionary, UriComponentsBuilder ucBuilder) {
        LOGGER.info("Creating MessageMapDictionary " + messageMapDictionary);

        messageResponseService.save(messageMapDictionary);

        HttpHeaders headers = new HttpHeaders();
        headers.setLocation(ucBuilder.path("/message/{id}").buildAndExpand(messageMapDictionary.getId()).toUri());
        return new ResponseEntity<Void>(headers, HttpStatus.CREATED);
    }
}
