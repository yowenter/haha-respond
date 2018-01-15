import $http from './const';

const register = (username, email) => {
  return $http
    .post('/api/user', { username, email })
    .then(res => res.data);
};

const join = (email, room) => {
  return $http.post('/api/join', {
    email,
    room,
  }).then(res => res.data);
};

export default {
  join,
  register,
};
