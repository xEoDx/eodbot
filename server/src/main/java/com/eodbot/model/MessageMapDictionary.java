package com.eodbot.model;


import javax.persistence.*;
import java.io.Serializable;
import java.util.Collections;
import java.util.List;

/**
 * Created by Victor on 18/07/2016.
 */
@Entity
@Table(name = "messagemapdictionary")
public class MessageMapDictionary implements Serializable {

    @Id
    @Column(name = "id")
    @GeneratedValue
    private Long id;

    @Column(name = "message_key")
    private String key;

    @ElementCollection(targetClass = String.class)
    @Column(name = "responses")
    private List<String> responses;

    public MessageMapDictionary() {
        this(0, "", Collections.EMPTY_LIST);
    }

    public MessageMapDictionary(long id, String key, List<String> responses) {
        this.id = id;
        this.key = key;
        this.responses = responses;
    }

    public Long getId() {
        return id;
    }

    public String getKey() {
        return key;
    }

    public List<String> getResponses() {
        return responses;
    }

    public void setId(long id) {
        this.id = id;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public void setResponses(List<String> responses) {
        this.responses = responses;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        MessageMapDictionary that = (MessageMapDictionary) o;

        return id == that.id;
    }

    @Override
    public int hashCode() {
        return (int) (id ^ (id >>> 32));
    }

    @Override
    public String toString() {
        return "MessageMapDictionary{" +
                "id=" + id +
                ", key='" + key + '\'' +
                ", responses=" + responses +
                '}';
    }
}
