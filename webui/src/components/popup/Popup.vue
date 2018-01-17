<template src="./Popup.html"></template>

<script>
import { bus } from '@/model/const';
import api from '@/model/api';
import { TimelineLite, Elastic, SlowMo, Power3 } from '@/components/popup/TweenMax.min';

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
      this.$nextTick(() => this.init());
    });
  },
  methods: {
    // 倒计时
    countdown() {
      this.sec = 10;
      const id = setInterval(() => {
        if (this.sec !== 0) {
          this.sec = this.sec - 1;
        } else {
          clearInterval(id);
          setTimeout(() => {
            this.hidePopup();
          }, 2000);
        }
      }, 1000);
    },
    // 点击选答案
    choose(item) {
      if (this.choice || !this.sec) return;
      this.choice = item.choice_id;
      this.endTime = (new Date).getTime(); // eslint-disable-line
      let score = 1 - ((this.endTime - this.startTime) / 10000);
      score = item.is_right ? (score + 1) : score;
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
    // 关闭 popup
    hidePopup() {
      this.show = false;
      this.startTime = null;
      this.endTime = null;
      this.choice = null;
      // 关闭题目时，刷新一下 rank 列表
      bus.$emit('user_vote');
    },
    // 点击动画
    /* eslint-disable */
    init() {
      function getRandom(min, max) {
        return Math.random() * (max - min) + min;
      }

      var isSafari = /constructor/i.test(window.HTMLElement);
      var isFF = !!navigator.userAgent.match(/firefox/i);

      if (isSafari) {
        document.getElementsByTagName('html')[0].classList.add('safari');
      }

      // Remove click on button for demo purpose
      // Array.prototype.slice.call(document.querySelectorAll('.option'), 0).forEach(function(bt) {
      //   bt.addEventListener('click', function(e) {
      //     e.preventDefault();
      //   });
      // });

      initBt2();

      // Button 2
      function initBt2() {
        let animation = false;
        Array.prototype.slice.call(document.querySelectorAll('.option'), 0).forEach(function(bt) {
          var filter = document.querySelectorAll('#filter-goo-2 feGaussianBlur')[0];
          var particleCount = 12;
          var colors = ['#DE8AA0', '#8AAEDE', '#FFB300', '#60C7DA']

          bt.addEventListener('click', function() {
            if (animation) return;
            animation = true;
            var particles = [];
            var tl = new TimelineLite({onUpdate: function() {
              filter.setAttribute('x', 0);
            }});

            tl.to(bt.querySelectorAll('.button__bg'), 0.6, { scaleX: 1.05 });
            tl.to(bt.querySelectorAll('.button__bg'), 0.9, { scale: 1, ease: Elastic.easeOut.config(1.2, 0.4) }, 0.6);

            for (var i = 0; i < particleCount; i++) {
              particles.push(document.createElement('span'));
              bt.appendChild(particles[i]);

              particles[i].classList.add(i % 2 ? 'left' : 'right');

              var dir = i % 2 ? '-' : '+';
              var r = i % 2 ? getRandom(-1, 1)*i/2 : getRandom(-1, 1)*i;
              var size = i < 2 ? 1 : getRandom(0.4, 0.8);
              var tl = new TimelineLite({ onComplete: function(i) {
                particles[i].parentNode.removeChild(particles[i]);
                this.kill();
              }, onCompleteParams: [i] });

              tl.set(particles[i], { scale: size });
              tl.to(particles[i], 0.6, { x: dir + 20, scaleX: 3, ease: SlowMo.ease.config(0.1, 0.7, false) });
              tl.to(particles[i], 0.1, { scale: size, x: dir +'=25' }, '-=0.1');
              if(i >= 2) tl.set(particles[i], { backgroundColor: colors[Math.round(getRandom(0, 3))] });
              tl.to(particles[i], 0.6, { x: dir + getRandom(60, 100), y: r*10, scale: 0.1, ease: Power3.easeOut });
              tl.to(particles[i], 0.2, { opacity: 0, ease: Power3.easeOut }, '-=0.2');
            }
          });
        });
      }
    },
  },
};
</script>

<style lang="scss" src="./distortedButton.scss"></style>
<style lang="scss" src="./Popup.scss"></style>
