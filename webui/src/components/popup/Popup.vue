<template src="./Popup.html"></template>

<script>
import { bus } from '@/model/const';
import api from '@/model/api';

export default {
  name: 'Popup',
  data() {
    return {
      sec: 10,
      show: false,
      data: null,
      startTime: null,
      endTime: null,
    };
  },
  created() {

  },
  mounted() {
    bus.$on('data', data => {
      console.log('data', data);
      this.data = data;
      this.show = true;
      this.countdown();
      this.startTime = (new Date).getTime(); // eslint-disable-line
    });
  },
  methods: {
    // 倒计时
    countdown() {
      const id = setInterval(() => {
        if (this.sec !== 0) {
          this.sec = this.sec - 1;
        } else {
          clearInterval(id);
          // this.show = false;
        }
      }, 1000);
    },
    // 点击选答案
    choose(item) {
      this.endTime = (new Date).getTime(); // eslint-disable-line
      let score = 1 - ((this.endTime - this.startTime) / 10000);
      score = item.is_right && (score + 1);
      api.vote({
        email: localStorage.getItem('email'),
        examId: localStorage.getItem('exam_id'),
        choiceId: item.choice_id,
        questionId: this.data.question_id,
        score,
      }).then(res => {
        console.log(res);
      });
    },
  },
};
</script>

<style lang="scss" src="./Popup.scss"></style>
