<template src="./Rank.html">
</template>

<script>
import { clone } from 'lodash';
import api from '@/model/api';

import { bus } from '@/model/const';

import TextAvatar from '../text-avatar';

export default {
  name: 'Rank',
  components: {
    TextAvatar,
  },
  data() {
    return {
      colors: [
        '#008bb9',
        '#05A4D8',
        '#1ED5F1',
        '#0B77CA',
      ],
      colors2: [
        '#da381b',
        '#e86f3c',
        '#f3b00f',
      ],
      topColors: [
        'rgba(218, 56, 27, 0.5)',
        'rgba(232, 111, 60, 0.6)',
        'rgba(243, 176, 15, 0.7)',
      ],
      topNameColors: [
        'rgb(218, 56, 27)',
        'rgb(232, 111, 60)',
        'rgb(243, 176, 15)',
      ],
      randomColorNumber: 4,
      ranks: [],
    };
  },
  created() {
    this.getRanks();
    bus.$on('user_vote', () => {
      this.getRanks();
    })
  },
  computed: {
    sortedRanks() {
      return clone(this.ranks).sort((a, b) => b.total_score - a.total_score);
    },
    topRanks() {
      return this.sortedRanks.slice(0, 3);
    },
    otherRanks() {
      return this.sortedRanks.slice(3);
    },
  },
  methods: {
    getRanks() {
      api.rank()
        .then(res => {
          this.ranks = res;
        });
    },
    getIcon(username, index, isTop = false, otherData = {}) {
      const colors = isTop ? this.colors2 : this.colors;
      const randomColorNumber = isTop ? 3 : this.randomColorNumber;
      return {
        text: username.slice(0, 1),
        color: '#ffffff',
        bg: colors[index % randomColorNumber],
        ...otherData,
      };
    },
  },
};
</script>

<style lang="scss" src="./Rank.scss"></style>
