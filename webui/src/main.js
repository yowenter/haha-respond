// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import '@babel/polyfill';
import Vue from 'vue';
import Vant from 'vant';
import 'vant/lib/vant-css/index.css';

import App from './App';
import router from './router';

require('es6-promise').polyfill();

Vue.config.productionTip = false;

Vue.use(Vant);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
