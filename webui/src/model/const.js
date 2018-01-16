import Vue from 'vue';
import axios from 'axios';

// API_URL
const defaultUrl = 'http://192.168.1.70:8088';
let currentUrl = defaultUrl;
if (process.env.API_URL) {
  currentUrl = process.env.API_URL;
  // API_URL 不能是 /, 否则最终 XHR 的请求 url 就变成了 http://api/networks 这样
  if (process.env.API_URL === '/') {
    currentUrl = '.';
  }
}
Vue.prototype.API_URL = currentUrl;

const $http = axios.create({
  baseURL: currentUrl,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default $http;
export const API_URL = currentUrl;
export const bus = new Vue(); // 空的 Vue 实例作为一个事件总线中心
