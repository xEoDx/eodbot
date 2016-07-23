package com.eodbot.configuration;

import com.eodbot.service.MessageResponseService;
import com.eodbot.service.MessageResponseServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * Created by Victor on 18/07/2016.
 */
@Configuration
public class AppConfiguration {
    @Bean
    public MessageResponseService messageResponseService() {
        return new MessageResponseServiceImpl();
    }


}
