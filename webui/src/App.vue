<template>
  <div id="app">
    <router-view/>
    <popup></popup>
  </div>
</template>

<script>
import popup from '@/components/popup/popup'; // eslint-disable-line

export default {
  name: 'App',
  components: {
    popup,
  },
};
</script>

<style>
  * {
    box-sizing: border-box;
  }
  /* van-tab */
  .van-tab--active {
    color: #05A4D8;
  }
  .van-tabs__nav-bar {
    background-color: #05A4D8;
  }
  .van-button--primary {
    background-color: #05A4D8;
    border: 1px solid #008bb9;
  }
</style>
