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

      const emailRegex = new RegExp(/(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/); // eslint-disable-line

      if (!name || !email) {
        this.showDialog('昵称及邮箱均不能为空');
        return false;
      } else if (!emailRegex.test(email)) {
        this.showDialog('邮箱格式错误');
        return false;
      }

      return true;
    },
    showDialog(text) {
      Dialog.alert({
        message: text,
      }).then(() => {
        // on close
      });
    },
    submit() {
      const valid = this.checkValid();
      if (valid) {
        // reg api
      }
    },
  },
};
</script>

<style lang="scss" src="./Reg.scss"></style>
