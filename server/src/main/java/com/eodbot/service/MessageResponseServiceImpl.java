package com.eodbot.service;

import com.eodbot.model.MessageMapDictionary;
import com.eodbot.repository.MessageResponseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 * Created by Victor on 18/07/2016.
 */
@Service
@Transactional
public class MessageResponseServiceImpl implements MessageResponseService {
    @Autowired
    private MessageResponseRepository messageResponseRepository;

    @Override
    public void save(MessageMapDictionary messageMapDictionary) {
        messageResponseRepository.save(messageMapDictionary);
    }

    @Override
    public List<MessageMapDictionary> findAll() {
        return (List<MessageMapDictionary>) messageResponseRepository.findAll();
    }

    @Override
    public MessageMapDictionary findById(Long id) {
        return messageResponseRepository.findOne(id);
    }
}
