import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index/Index';
import Reg from '@/components/Reg/Reg';
import Board from '@/components/Board/Board';

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
    {
      path: '/board',
      name: 'Board',
      component: Board,
    },
  ],
});
