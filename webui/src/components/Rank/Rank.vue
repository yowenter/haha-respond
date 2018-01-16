<template src="./Rank.html">
</template>

<script>
import { clone } from 'lodash';

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
      topColors: [
        'rgb(170,170,170)',
        'rgb(245,193,105)',
        'rgba(194,9,9,0.5)',
      ],
      randomColorNumber: 7,
      ranks: [{
        username: 'Test1',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Cin2',
        email: 'aa@daocloud.io',
        score: 112,
      }, {
        username: 'Mimo3',
        email: 'aa@daocloud.io',
        score: 113,
      }, {
        username: 'Nighting4',
        email: 'aa@daocloud.io',
        score: 114,
      }, {
        username: 'Cisy5',
        email: 'aa@daocloud.io',
        score: 115,
      }, {
        username: 'Test',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Test2',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Test3',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Test4',
        email: 'aa@daocloud.io',
        score: 111,
      }, {
        username: 'Test5',
        email: 'aa@daocloud.io',
        score: 111,
      }],
    };
  },
  computed: {
    sortedRanks() {
      return clone(this.ranks).sort((a, b) => b.score - a.score);
    },
    topRanks() {
      const topRanks = this.sortedRanks.slice(0, 3);
      return [{
        index: 2,
        ...topRanks[1],
      }, {
        index: 1,
        ...topRanks[0],
      }, {
        index: 3,
        ...topRanks[2],
      }];
    },
    otherRanks() {
      return this.sortedRanks.slice(3);
    },
  },
  mounted() {
    // const user = localStorage.getItem('user');
    // if (!user) {
    //   this.$router.push({ name: 'Register' });
    // }
  },
  methods: {
    getIcon(username, index, otherData = {}) {
      return {
        text: username.slice(0, 1),
        color: '#ffffff',
        bg: this.colors[index % this.randomColorNumber],
        ...otherData,
      };
    },
  },
};
</script>

<style lang="scss" src="./Rank.scss"></style>
