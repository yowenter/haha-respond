<template>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
    <defs>
      <filter id="f1" x="-1" y="-1" width="300%" height="300%">
        <feGaussianBlur in="SourceAlpha" stdDeviation="8" />
        <feOffset result="offsetblur" dx="0" dy="0" />
        <feFlood flood-color="rgba(0,0,0,0.2)"/>
        <feComposite in2="offsetblur" operator="in"/>
        <feMerge>
          <feMergeNode/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
      <filter id="f2" x="-1" y="-1" width="300%" height="300%">
        <feGaussianBlur in="SourceAlpha" stdDeviation="1" />
        <feOffset result="offsetblur" dx="0" dy="0" />
        <feFlood flood-color="rgba(0,0,0,0.3)"/>
        <feComposite in2="offsetblur" operator="in"/>
        <feMerge>
          <feMergeNode/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <rect x="20" y="20" rx="10" ry="10" width="60" height="60"
      stroke="white" stroke-width="2.5"
      transform="rotate(45, 50 50)" filter="url(#f2)"
      :style="{fill: currentData.bg}"/>
    <rect x="20" y="20" rx="10" ry="10" width="60" height="60"
      stroke="white" stroke-width="2.5"
      transform="rotate(45, 50 50)" filter="url(#f1)"
      :style="{fill: currentData.bg}"/>
    <text text-anchor="middle" y="50%" x="50%" dy="0.35em"
      :fill="currentData.color" :font-size="fontSize"
      style="font-weight: 400;">{{currentData.text}}</text>
  </svg>
</template>

<script>
export default {
  name: 'TextAvatar',
  props: ['data'],
  data() {
    return {
      currentData: {
        text: '匿',
        color: '#ffffff',
        bg: '#3890ff',
      },
    };
  },
  created() {
    this.setCurrentData(this.data);
  },
  watch: {
    data(val) {
      this.setCurrentData(val);
    },
  },
  computed: {
    fontSize() {
      const len = this.currentData.text.length;
      if (len === 1 || len === 0) {
        return 35;
      }
      return 100 / len;
    },
  },
  methods: {
    setCurrentData(val) {
      if (!val) return;
      this.currentData = val;
    },
  },
};
</script>
