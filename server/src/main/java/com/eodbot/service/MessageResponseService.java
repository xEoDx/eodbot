package com.eodbot.service;

import com.eodbot.model.MessageMapDictionary;

import java.util.List;

/**
 * Created by Victor on 18/07/2016.
 */
public interface MessageResponseService {
    void save(MessageMapDictionary messageMapDictionary);
    List<MessageMapDictionary> findAll();
    MessageMapDictionary findById(Long id);
}
