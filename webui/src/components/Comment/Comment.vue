<template>
  <div class="comments-wrapper">
    <div class="comments">
      <div class="waves">
        <div class="wave wave_1"></div>
        <div class="wave wave_2"></div>
        <div class="wave wave_3"></div>
        <div class="wave wave_4"></div>
        <div class="wave wave_5"></div>
      </div>
      <ul class="comment-list">
        <li v-for="message in messages" :key="message.time" class="comment">
          <span class="name">{{ message.user }}</span><!--
          --><span class="message">{{ message.message }}</span>
        </li>
      </ul>
    </div>
    <van-icon name="chat" class="chat-icon" @click="showCommentBox"/>
    <comment-box :show="show" @closed="closeCommentBox"></comment-box>
  </div>
</template>

<script>
import { bus } from '@/model/const';
import CommentBox from '@/components/CommentBox/CommentBox';

export default {
  name: 'Comment',
  components: {
    CommentBox,
  },
  data() {
    return {
      messages: [],
      show: false,
    };
  },
  mounted() {
    bus.$on('comment', info => {
      this.messages.push(info);
      this.judgeLength();
      this.$nextTick(() => {
        const commentList = document.getElementsByClassName('comment-list')[0];
        commentList.scrollTop = commentList.scrollHeight;
      });
    });
  },
  methods: {
    judgeLength() {
      const length = this.messages.length;
      if (length > 100) {
        this.messages = this.messages.slice(length - 100, length);
      }
    },
    showCommentBox() {
      this.show = true;
    },
    closeCommentBox() {
      this.show = false;
    },
  },
};
</script>

<style lang="scss">
.comments-wrapper {
  position: fixed;
  bottom: 0;
  left: 0;
  height: 200px;
  width: 100%;
  z-index: 1000;
}

.comments {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 200px;
  width: 100%;
  background: rgba(5, 164, 216, 0.6);
  z-index: 1000;
  -webkit-mask-image: -webkit-gradient(linear, 0% 0%, 0% 20%,from(transparent), to(#ffffff));
  opacity: 0.8;
}

.comment-list {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding-bottom: 10px;
  z-index: 18;
  overflow-y: scroll;

  .comment:first-child {
    padding-top: 40px;
  }

  .comment {
    padding: 0 10px;
    display: flex;
  }

  .comment span {
    display: inline-block;
    margin-left: 5px;
  }

  .comment .name {
    color: #004179;
  }

  .comment .message {
    color: #fff;
    word-break: break-all;
  }
}

.comment-list::-webkit-scrollbar {
  display: none;
}

.chat-icon {
  position: absolute;
  bottom: 15px;
  right: 15px;
  z-index: 1001;
  font-size: 30px;
  color: #fff;
  opacity: 0.7;
}

.waves {
  width: 100%;
  height: 50%;
  position: absolute;
  overflow: hidden;
  bottom: 0;
  left: 0;
}

.wave {
  width:calc( 100% + 4em );
  height:100%;
  position:absolute;
  left:-2em;
  background:bottom center repeat-x;
  background-size: 26%;
  animation-iteration-count:infinite;
  animation-timing-function:linear;
  @media (max-width: 480px) {
    background-size: 52%;
  }
}

/* Individual wave layers */

.wave_1 {
  animation-name:wave_1;
  animation-duration:3400ms;
  animation-delay:-1200ms;
  top:5px;
  z-index:1;
  opacity:0.1;
  background-image:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="246" height="2000" viewBox="0 0 246 2000"><g transform="rotate(180 123 1000) scale(0.5 1)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 2000c50.43 0 72.57-20.522 123-20.522 50.43 0 71.34 20.522 123 20.522V0H0v2000z"/></g><g transform="rotate(180 123 1000) scale(0.5 1) translate(246 0)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 2000c50.43 0 72.57-20.522 123-20.522 50.43 0 71.34 20.522 123 20.522V0H0v2000z"/></g></svg>');
  background-position:top left;
}

.wave_2 {
  animation-name:wave_2;
  animation-duration:3200ms;
  animation-delay:-600ms;
  top:15px;
  z-index:2;
  opacity:0.2;
  background-image:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="307" height="2000" viewBox="0 0 307 2000"><g transform="rotate(180 153.5 1000) scale(0.5 1)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 0h307v2000c-64.47 0-90.563-25.623-153.5-25.623C90.565 1974.377 62.935 2000 0 2000V0z"/></g><g transform="rotate(180 153.5 1000) scale(0.5 1) translate(307 0)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 0h307v2000c-64.47 0-90.563-25.623-153.5-25.623C90.565 1974.377 62.935 2000 0 2000V0z"/></g></svg>');
  background-position:top right;
}

.wave_3
{
  animation-name:wave_3;
  animation-duration:2800ms;
  animation-delay:-2400ms;
  top:25px;
  z-index:3;
  opacity:0.3;
  background-image:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="384" height="2000" viewBox="0 0 384 2000"><g transform="rotate(180 192 1000) scale(0.5 1)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 0h384v2000c-80.64 0-113.28-32.047-192-32.047S78.72 2000 0 2000V0z"/></g><g transform="rotate(180 192 1000) scale(0.5 1) translate(384 0)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 0h384v2000c-80.64 0-113.28-32.047-192-32.047S78.72 2000 0 2000V0z"/></g></svg>');
  background-position:top center;
}

.wave_4
{
  animation-name:wave_4;
  animation-duration:2600ms;
  animation-delay:-1800ms;
  top:35px;
  z-index:4;
  opacity:0.4;
  background-image:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="480" height="2000" viewBox="0 0 480 2000"><g transform="rotate(180 240 1000) scale(0.5 1)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M480 2000c-100.8 0-141.6-39.892-240-39.892S98.4 2000 0 2000V0h480v2000z"/></g><g transform="rotate(180 240 1000) scale(0.5 1) translate(480 0)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M480 2000c-100.8 0-141.6-39.892-240-39.892S98.4 2000 0 2000V0h480v2000z"/></g></svg>');
  background-position:top left;
}

.wave_5
{
  animation-name:wave_5;
  animation-duration:3000ms;
  animation-delay:-3000ms;
  top:45px;
  z-index:5;
  opacity:0.5;
  background-image:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="600" height="2000" viewBox="0 0 600 2000"><g transform="rotate(180 300 1000) scale(0.5 1)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 2000c123 0 177-49.866 300-49.866S474 2000 600 2000V0H0v2000z"/></g><g transform="rotate(180 300 1000) scale(0.5 1) translate(600 0)"><path fill-rule="evenodd" clip-rule="evenodd" fill="#05A4D8" d="M0 2000c123 0 177-49.866 300-49.866S474 2000 600 2000V0H0v2000z"/></g></svg>');
  background-position:top right;
}

/* Wave animations */

@keyframes wave_1 {
  from { transform: rotate(0deg) translatey(-10px) rotate(0deg); }
  to { transform: rotate(360deg) translatey(-10px) rotate(-360deg) ; }
}

@keyframes wave_2 {
  from { transform: rotate(0deg) translatey(-12px) rotate(0deg); }
  to { transform: rotate(360deg) translatey(-12px) rotate(-360deg) ; }
}

@keyframes wave_3 {
  from { transform: rotate(0deg) translatey(-15px) rotate(0deg); }
  to { transform: rotate(360deg) translatey(-15px) rotate(-360deg) ; }
}

@keyframes wave_4 {
  from { transform: rotate(0deg) translatey(-18px) rotate(0deg); }
  to { transform: rotate(360deg) translatey(-18px) rotate(-360deg) ; }
}

@keyframes wave_5 {
  from { transform: rotate(0deg) translatey(-20px) rotate(0deg); }
  to { transform: rotate(360deg) translatey(-20px) rotate(-360deg) ; }
}

.sea {
  background: #05A4D8;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 30%;
  opacity: 0.75;
}
</style>
