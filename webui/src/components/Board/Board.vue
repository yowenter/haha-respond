<template src="./Board.html"></template>

<script>
// 连接 websocket
import '@/model/socket';

import Rank from '../Rank/Rank';
import Comment from '../Comment/Comment';

export default {
  name: 'Board',
  components: {
    Rank,
    Comment,
  },
  data() {
    return {

    };
  },
  methods: {

  },
};
</script>

<style lang="scss" src="./Board.scss"></style>
