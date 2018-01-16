<template src="./Board.html"></template>

<script>
// 连接 websocket
import '@/model/socket';
import { bus } from '@/model/const';

import Rank from '../Rank/Rank';

export default {
  name: 'Board',
  components: {
    Rank,
  },
  data() {
    return {

    };
  },
  methods: {
    // 测试用，最后删掉
    popup() {
      bus.$emit('data', {
        question_id: '1XX',
        question_text: 'XXXXXXXXXXXXXXXXXXXXXXXX',
        choices: [
          {
            choice_id: 'XXX',
            choice_text: 'XXXX',
            is_right: true,
          },
          {
            choice_id: 'XXX',
            choice_text: 'XXXX',
            is_right: false,
          },
          {
            choice_id: 'XXX',
            choice_text: 'XXXX',
            is_right: false,
          },
        ],
      });
    },
  },
};
</script>

<style lang="scss" src="./Board.scss"></style>
