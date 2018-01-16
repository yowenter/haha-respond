import io from 'socket.io-client';
import { API_URL, bus } from '@/model/const';

const url = API_URL === '.' ? '' : API_URL;
const roomId = localStorage.getItem('room_id');
const commentRoomId = '88888';

let socket;

if (socket) socket.disconnect();
socket = io(`${url}`, {
  path: '/stream/socket.io',
});
socket.on('connect', () => {
  socket.emit('enter_room', roomId);
  console.log('enter_room');
});
socket.on('question_update', data => {
  console.log('data', data);
  bus.$emit('data', data);
});
socket.on('disconnect', () => {
  console.log('disconnect');
});

let commentSocket;

if (commentSocket) commentSocket.disconnect();
commentSocket = io(`${url}`, {
  path: '/danmus/socket.io',
});
commentSocket.on('connect', () => {
  commentSocket.emit('enter_room', commentRoomId);
  console.log('enter_comment_room');
});
commentSocket.on('comment', data => {
  console.log('comment', data);
  bus.$emit('comment', data);
});
commentSocket.on('disconnect', () => {
  console.log('comment_disconnect');
});
