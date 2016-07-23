package com.eodbot.repository;

import com.eodbot.model.MessageMapDictionary;
import org.springframework.data.repository.CrudRepository;

/**
 * Created by Victor on 18/07/2016.
 */
public interface MessageResponseRepository extends CrudRepository<MessageMapDictionary, Long> {

}
