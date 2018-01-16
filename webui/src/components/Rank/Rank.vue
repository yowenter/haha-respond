<template src="./Rank.html"></template>

<script>
import TextAvatar from '../text-avatar';

export default {
  name: 'Rank',
  components: {
    TextAvatar,
  },
  data() {
    return {
      colors: [
        '#FBA3ED',
        '#F69876',
        '#3FCF8F',
        '#F5C169',
        '#7A9ACF',
        '#53C0CA',
        '#85C486',
      ],
      randomColorNumber: 7,
      ranks: [{
        username: 'Test1',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Cin2',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Mimo3',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Nighting4',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Cisy5',
        email: 'aa@daocloud.io',
        score: 111,
      }],
    };
  },
  mounted() {
    // const user = localStorage.getItem('user');
    // if (!user) {
    //   this.$router.push({ name: 'Register' });
    // }
  },
  methods: {
    getIcon(username, index) {
      return {
        text: username.slice(0, 1),
        color: '#ffffff',
        bg: this.colors[index % this.randomColorNumber],
      };
    },
  },
};
</script>

<style lang="scss" src="./Rank.scss"></style>
