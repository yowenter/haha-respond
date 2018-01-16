import io from 'socket.io-client';
import { API_URL, bus } from '@/model/const';

const url = API_URL === '.' ? '' : API_URL;
const roomId = localStorage.getItem('room_id');

let socket;

if (socket) socket.disconnect();
socket = io(`${url}/`, {
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
