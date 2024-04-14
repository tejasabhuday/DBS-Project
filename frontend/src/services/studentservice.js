import axios from 'axios';

export function getStudents() {
  return axios.get('http://127.0.0.1:8000/students/')
    .then(response => response.data)
}
export function updateStudent(stuid, student) {
  return axios.put('http://127.0.0.1:8000/students/' + stuid + '/', {
    FirstName:student.FirstName.value,
    LastName:student.LastName.value,
    RegisterationNumber:student.RegisterationNumber.value,
    insidehostel:student.insidehostel.value,
  })
   .then(response => response.data)
}