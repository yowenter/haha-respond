<template>
  <div class="code">
    <!-- 密码输入框 -->
    <van-password-input
      :value="code"
      :length="4"
      info="请输入 4 位邀请码"
      :error-info="error"
      @focus="showKeyboard = true"
    />

    <!-- 数字键盘 -->
    <van-number-keyboard
      :show="showKeyboard"
      @input="onInput"
      @delete="onDelete"
      @blur="showKeyboard = false"
    />
  </div>
</template>

<script>
import api from '@/model/api';

export default {
  name: 'Code',
  data() {
    return {
      code: '',
      showKeyboard: true,
      error: '',
    };
  },
  methods: {
    onInput(key) {
      this.code = (this.code + key).slice(0, 4);
      if (this.code.length === 4) {
        this.submit(this.code);
      }
    },
    onDelete() {
      this.code = this.code.slice(0, this.code.length - 1);
    },
    submit(code) {
      const email = localStorage.getItem('user');
      api.join(email, code).then(res => {
        localStorage.setItem('room_id', res.room_id);
        this.$router.push({ name: 'Board' });
      }, () => {
        this.code = '';
        this.error = '邀请码错误';
      });
    },
  },
};
</script>

<style lang="scss">
.code {
  margin-top: 40%;
}
</style>
