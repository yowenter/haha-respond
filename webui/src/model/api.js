import $http from './const';

const comment = (data) => {
  return $http.post('/comments', {
    event: 'comment',
    data,
  }).then(res => res.data);
};

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

const vote = (email, examId, choiceId, questionId, score) => {
  return $http.post('/api/join', {
    email, exam_id: examId, choice_id: choiceId, question_id: questionId, score,
  }).then(res => res.data);
};

export default {
  comment,
  join,
  register,
  vote,
};
