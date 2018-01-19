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
    const roomId = localStorage.getItem('room_id');
    if (!user) {
      this.$router.push({ name: 'Register' });
    } else if (!roomId) {
      this.$router.push({ name: 'Code' });
    }

    initSocket();
  },
};
</script>

<style lang="scss" src="./Board.scss"></style>
