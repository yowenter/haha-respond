<template>
  <div class="index">
    <div class="bg-wrapper">
      <img class="bg" :src="bg">
    </div>
    <div class="qrcode-wrapper">
      <img class="qrcode" :src="qrcode">
    </div>
  </div>
</template>

<script>
import bg from '@/assets/bg.gif';
import qrcode from '@/assets/qrcode.jpeg';

export default {
  name: 'Index',
  data() {
    return {
      bg,
      qrcode,
    };
  },
};
</script>

<style lang="scss">
html, body {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
  background: #000000;
}
.index, .bg-wrapper,  .qrcode-wrapper {
  height: 100%;
  width: 100%;
}
.bg-wrapper, .qrcode-wrapper {
  display: flex;
  justify-content: center;
  align-content: center;
  align-items: center;
}
.qrcode-wrapper {
  position: absolute;
  top: 0;
  left: 0;
}
.bg {
  width: 800px;
  height: 600px;
}
.qrcode {
  margin-top: 30px;
  margin-right: 10px;
  width: 200px;
  height: 200px;
}
</style>
