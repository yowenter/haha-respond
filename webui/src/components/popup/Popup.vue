<template src="./Popup.html"></template>

<script>
import { bus } from '@/model/const';
import api from '@/model/api';
import { Toast } from 'vant';

export default {
  name: 'Popup',
  data() {
    return {
      sec: 10,
      show: false,
      data: null,
      startTime: null,
      endTime: null,
      choice: null,
      score: 0,
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
      this.rightId = data.choices.find(res => res.is_right).choice_id;
      console.log('rightId', this.rightId);
    });
  },
  computed: {
    isRight() {
      return this.choice && this.rightId && this.rightId === this.choice;
    },
  },
  methods: {
    // 倒计时
    countdown() {
      this.sec = 10;
      const id = setInterval(() => {
        this.countdownAnimation(this.sec);
        if (this.sec !== 0) {
          this.sec = this.sec - 1;
        } else {
          clearInterval(id);
          setTimeout(() => {
            if (this.score) {
              Toast(`恭喜答对了，加 ${this.score} 分`);
            }
            this.hidePopup();
          }, 2000);
        }
      }, 1000);
    },
    // 倒计时动画
    countdownAnimation(countdown) {
      const circle = document.querySelectorAll('circle')[1];
      const percent = (11 - countdown) / 10;
      const perimeter = Math.PI * 2 * 35;
      if (percent > 6 / 10) {
        circle.setAttribute('stroke', 'rgb(255,135,135)');
      }
      circle.setAttribute('stroke-dasharray', `${perimeter * percent} ${perimeter * (1 - percent)}`);
    },
    // 点击选答案
    choose(item) {
      if (this.choice || !this.sec) return;
      this.choice = item.choice_id;
      this.endTime = (new Date).getTime(); // eslint-disable-line
      const total = item.is_last_question ? 200 : 100; // 最后一题分数 double
      let score = ((this.endTime - this.startTime) * total) / 10000;
      score = item.is_right ? score.toFixed() : 0;
      api.vote({
        email: localStorage.getItem('email'),
        examId: localStorage.getItem('exam_id'),
        choiceId: item.choice_id,
        questionId: this.data.question_id,
        score,
      }).then(res => {
        this.score = score;
        console.log(res);
      });
    },
    // 关闭 popup
    hidePopup() {
      const circle = document.querySelectorAll('circle')[1];
      circle.setAttribute('stroke', 'rgb(77,171,247)');
      this.show = false;
      this.startTime = null;
      this.endTime = null;
      this.choice = null;
      this.score = 0;
      // 关闭题目时，刷新一下 rank 列表
      bus.$emit('user_vote');
    },

  },
};
</script>

<style lang="scss" src="./Popup.scss" scoped></style>
