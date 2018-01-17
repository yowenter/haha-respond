<template>
  <div class="comment" :style="transStyle" ref="comment">
      <span class="user">{{ data.user }}</span>
      <span class="message">{{ data.message }}</span>
    </div>
</template>

<script>
export default {
  name: 'Comment',
  props: ['data', 'index'],
  data() {
    return {
      clientWidth: 0,
      clientHeight: 0,
      divWidth: 0,
      divHeight: 0,
      startTime: 0,
      speed: 100,
      transStyle: '',
    };
  },
  mounted() {
    this.startTime = +new Date();
    this.divWidth = parseInt(window.getComputedStyle(this.$refs.comment).width, 10) + 50;
    this.divHeight = Math.floor(Math.random() * this.clientHeight);
  },
  created() {
    this.clientWidth = parseInt(document.body.clientWidth, 10);
    this.clientHeight = parseInt(document.body.clientHeight, 10) - 200;
    requestAnimationFrame(this.setTransStyle);
  },
  methods: {
    setTransStyle() {
      const leftTime = (+new Date() - this.startTime) / 1000;
      const transformX = this.clientWidth - (this.speed * leftTime);
      this.transStyle = `transform: translate3d(${transformX}px, ${this.divHeight}px, 0)`;

      if (transformX > -this.divWidth) {
        requestAnimationFrame(this.setTransStyle);
      } else {
        this.$emit('end', this.index);
      }
    },
  },
};
</script>

<style lang="scss">
.comments .comment {
  display: inline-block;
  background-color: #02e8f0;
  border-radius: 100000px;

  span {
    color: #fff;
    display: inline-block;
    padding: 5px 10px;
  }

  .user {
    background-color: #074399;
    border-radius: 1000000px;
  }
}
</style>
