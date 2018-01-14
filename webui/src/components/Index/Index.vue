<template>
  <div>
    <van-loading type="gradient-circle" color="black" />
  </div>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
    };
  },
  mounted() {
    const user = localStorage.getItem('user');
    if (user) {
      // go to main page
    } else {
      this.$router.push({ name: 'Register' });
    }
  },
};
</script>

<style lang="scss">

</style>
