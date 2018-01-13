REST API
================

Haha Respond API



获取当前比赛状态
-----------------

.. http:get:: /v1/game

.. sourcecode:: http

    HTTP/1.1 200 OK

    {
        "id":"123",
        "started_at":"1515851260",
        "current_question": "XXXX",
        "user":{
            "id":"XXX",
            "state":"failure"
        }
    }


获取问题
-----------------

.. http:get:: /v1/question

    :jsonparam string token: token
    :jsonparam string game_id: game_123




提交答案
-----------------

.. http:post:: /v1/respond

    :jsonparam string token: token
    :jsonparam string game_id: game_123
    :jsonparam string answer: game_123



获取答案
------------------

.. http:get:: /v1/answer

    :jsonparam string token: token


消息推送问题
-----------------

**message**::

    {
            "id":"XXX",
            "question":"XXXX",
            "choices":{
                "A":"XXXX",
                "B":"XXXX",
                "C":"XXXXX"
            }
        }


消息推送答案
-------------------

**message**::

        {
            "id":"XXX",
            "question_id":"123",
            "answer":"A"
        }
