<template src="./Reg.html"></template>

<script>
import { Dialog } from 'vant';

export default {
  name: 'Register',
  data() {
    return {
      username: '',
      email: '',
      valid: {
        show: false,
        text: '',
      },
    };
  },
  methods: {
    checkValid() {
      const name = this.username;
      const email = this.email;

      if (!name || !email) {
        this.showDialog('昵称及邮箱均不能为空');
      }
    },
    showDialog(text) {
      Dialog.alert({
        message: text,
      }).then(() => {
        // on close
      });
    },
    submit() {
      this.checkValid();
    },
  },
};
</script>

<style lang="scss" src="./Reg.scss"></style>
