REST API
================

Haha Respond API



Signup
-------------

.. http:post:: /api/user

    :jsonparam string username: TAOG
    :jsonparam string email: TAOG@DAOCLOUD.IO


.. sourcecode:: http

    HTTP/1.1 200 OK



.. http:post:: /api/join

    :jsonparam string email: TAOG@DAOCLOUD.IO
    :jsonparam string room: 1234


.. sourcecode:: http

    HTTP/1.1 200 OK


    {
        "room_id":"123"
    }


.. http:get:: /api/exam

    :jsonparam string email: TAOG@DAOCLOUD.IO


.. sourcecode:: http

    HTTP/1.1 200 OK


    {
        "room_id":"123",
        "exam":{
            "exam_id":"1334",
            "state":"live",
            "question":{
                "question_id":"1XX",
                "question_text":"XXXXX",
                "choices":[
                    {
                        "choice_id":"XXX",
                        "choice_text":"XXXX",
                        "is_right":False
                    }
                ]
            }

        }
    }




.. http:post:: /api/votes

    :jsonparam string email: TAOG@DAOCLOUD.IO
    :jsonparam string exam_id: XXX
    :jsonparam string choice_id: XXX
    :jsonparam string question_id: XXX
    :jsonparam string score: XXX


.. sourcecode:: http

    HTTP/1.1 200 OK


Question 推送消息
----------------------


**Message**::

            {
                "question_id":"1XX",
                "question_text":"XXXXX",
                "choices":[
                    {
                        "choice_id":"XXX",
                        "choice_text":"XXXX",
                        "is_right":False
                    }
                ]
            }