<template src="./Board.html"></template>

<script>
// 连接 websocket
import initSocket from '@/model/socket';

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
  mounted() {
    const user = localStorage.getItem('email');
    if (!user) {
      this.$router.push({ name: 'Register' });
    }

    initSocket();
  },
};
</script>

<style lang="scss" src="./Board.scss"></style>
