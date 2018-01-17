<template>
  <div :class="{comment: true, gold: isRoby(data)}" :style="transStyle" ref="comment">
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
      roby: 'roby.chen@daocloud.io',
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
        this.$emit('end', this.data);
      }
    },
    isRoby(data) {
      if (data.email === this.roby) {
        return true;
      }
      return false;
    },
  },
};
</script>

<style lang="scss">
.comments .comment {
  display: inline-block;
  vertical-align: top;
  background-color: #21282b;
  border-radius: 4px;
  opacity: 0.8;

  span {
    color: #fff;
    display: inline-block;
    padding: 5px 0px 5px 10px;
  }

  .user {
    font-weight: 200;
    color: #e7edf9;
    vertical-align: top;
  }

  .message {
    color: #ffbb3e;
    font-weight: 200;
    padding-right: 10px;
    padding-left: 5px;
    vertical-align: top;
  }
  &.gold {
    .user {
      font-size: 24px;
      color: gold;
      word-break: keep-all;
    }

    .message {
      font-size: 24px;
      word-break: break-all;
      max-width: 600px;
    }
  }
}
</style>
