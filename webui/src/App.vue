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
</style>
