<template>
  <div class="comment-box">
    <van-popup v-model="visible" position="top" :overlay="true" class="input-field">
      <van-field
        v-model="message"
        type="textarea"
        placeholder="请输入评论"
        rows="1"
        autosize
      />
      <p v-if="error" class="error">{{ error }}</p>
      <van-button size="small" class="sub-button" type="primary" @click="submitMessage">提交</van-button>
    </van-popup>
  </div>
</template>

<script>
import api from '@/model/api';

export default {
  name: 'CommentBox',
  props: {
    show: {
      default: false,
    },
  },
  data() {
    return {
      visible: false,
      message: '',
      error: '',
    };
  },
  watch: {
    show(_new) {
      this.visible = _new;
    },
    visible(_new) {
      if (_new === false) {
        this.$emit('closed');
      }
    },
  },
  methods: {
    checkMessage() {
      const message = this.message;
      if (!message) {
        this.error = '不能提交空值';
        return false;
      }

      this.error = '';
      return true;
    },
    submitMessage() {
      const valid = this.checkMessage();
      const message = this.message;
      const user = localStorage.getItem('username');
      const email = localStorage.getItem('email');
      const time = +new Date();

      if (valid) {
        api.comment({
          message,
          user,
          email,
          time,
        }).then(() => {
          this.message = '';
          this.$emit('closed');
        }, () => {
          this.error = '提交失败';
        });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.van-popup.input-field {
  margin-top: 10%;
  padding-bottom: 10px;
}
.error {
  margin: 5px;
  color: red;
  font-size: 12px;
}
.comment-box .sub-button {
  margin-top: 10px;
  float: right;
}
</style>
