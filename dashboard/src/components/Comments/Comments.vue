<template>
  <div class="comments">
    <comment v-for="(co, index) in comments"
      :key="co.time"
      :data="co"
      :index="index"
      @end="destory"
    ></comment>
  </div>
</template>

<script>
import { bus } from '@/model/const';
import Comment from '@/components/Comment/Comment';

export default {
  name: 'Comments',
  components: {
    Comment,
  },
  data() {
    return {
      comments: [],
    };
  },
  mounted() {
    bus.$on('comment', (comment) => {
      this.comments.push(comment);
    });
  },
  methods: {
    destory(co) {
      let index = 0;
      this.comments.forEach((c, i) => {
        if (c.time === co.time && c.message === co.message && c.email === co.email) {
          index = i;
        }
      });
      this.comments.splice(index, 1);
    },
  },
};
</script>

<style lang="scss">
.comments {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99;
  overflow: hidden;
}
</style>
