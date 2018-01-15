import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/components/Index/Index';
import Reg from '@/components/Reg/Reg';
import Board from '@/components/Board/Board';
import Code from '@/components/Code/Code';
import Rank from '@/components/Rank/Rank';

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
    {
      path: '/code',
      name: 'Code',
      component: Code,
    },
    {
      path: '/rank',
      name: 'Rank',
      component: Rank,
    },
  ],
});
