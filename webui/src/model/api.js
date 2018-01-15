import $http from './const';

const register = (username, email) => {
  return $http.post('/api/user', {
    username,
    email,
  }).then(res => res.data);
};

export default {
  register,
};
