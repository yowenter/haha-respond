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
        'rgb(245,193,105)',
        'rgb(170,170,170)',
        'rgba(194,9,9,0.5)',
      ],
      randomColorNumber: 7,
      ranks: [],
    };
  },
  computed: {
    sortedRanks() {
      return clone(this.ranks).sort((a, b) => b.score - a.score);
    },
    topRanks() {
      return this.sortedRanks.slice(0, 3);
    },
    otherRanks() {
      return this.sortedRanks.slice(3);
    },
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
