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
    :jsonparam string room: 1234


.. sourcecode:: http

    HTTP/1.1 200 OK


    {
        "question": {
            "category": "Life",
            "difficulty": 1,
            "choices": [
                {
                    "choice_id": "1234",
                    "choice_text": "42",
                    "is_right": true
                },
                {
                    "choice_id": "1234",
                    "choice_text": "41",
                    "is_right": false
                },
                {
                    "choice_id": "1234",
                    "choice_text": "24",
                    "is_right": false
                }
            ],
            "question_text": "生命宇宙及一切的答案是什么？",
            "question_id": "1234"
        },
        "state": "live",
        "room_id": "1234"
    }



.. http:post:: /api/votes

    :jsonparam string email: TAOG@DAOCLOUD.IO
    :jsonparam string exam_id: XXX
    :jsonparam string choice_id: XXX
    :jsonparam string score: XXX


.. sourcecode:: http

    HTTP/1.1 200 OK

.. http:get:: /api/report

    :jsonparam string room: room



.. sourcecode:: http

    HTTP/1.1 200 OK

    [
        {
            "email":"TAOG@daocloud.io",
            "total_score":"123",
            "right_question_count":10,
            "username":"TAOG"
        }

    ]

.. http:post:: /comments

    :jsonparam string event: comment
    :jsonparam string data: {}

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



弹幕消息
------------------------

path /danmus/socket.io

enter_room room_id = '88888'

推送的消息类型为 RestApi 中的 event
推送的内容为 data 对应的内容