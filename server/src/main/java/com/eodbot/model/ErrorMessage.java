package com.eodbot.model;


import java.io.Serializable;

/**
 * Created by Victor on 10/08/2016.
 */
public class ErrorMessage implements Serializable {
    private final String message;

    public ErrorMessage(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    @Override
    public String toString() {
        return "ErrorMessage{" +
                "message='" + message + '\'' +
                '}';
    }
}
