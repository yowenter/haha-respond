import axios from 'axios';

const $http = axios.create({
  baseURL: 'http://192.168.1.70:8088',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default $http;
