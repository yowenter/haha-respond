import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index/Index';
import Reg from '@/components/Reg/Reg';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
    },
    {
      path: '/register',
      name: 'Register',
      component: Reg,
    },
  ],
});
