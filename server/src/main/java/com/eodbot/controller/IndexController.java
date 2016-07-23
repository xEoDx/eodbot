package com.eodbot.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Created by Victor on 18/07/2016.
 */
@Controller
@RequestMapping("/")
public class IndexController {
    private final static Logger LOGGER = LoggerFactory.getLogger(IndexController.class);

    @RequestMapping(method = RequestMethod.GET)
    public String getIndexPage() {
        LOGGER.info("Getting index page!");
        return "index";
    }


}
