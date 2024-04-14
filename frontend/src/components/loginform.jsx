
import './loginform.css';
import attendancepng from '../images/attendancepng.png';
/*const Loginform = () => {
  return (
        <form action=''>
            <div className='wrapper'>
                <img src={attendancepng}></img>
                <div className='inputdiv'>
                    <div className='inputno'>
                        <input placeholder='Registration No.' id='inputstyle'></input>
                    </div>
                </div>
                <div className='buttondiv'>
                    <button type='sumbit'>Sumbit</button>
                </div>
                <div className='admin'>
                    <a href="http://127.0.0.1:8000/admin/">admin login</a>
                </div>

            </div>
        </form>

  )
}
*/

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [RegisterationNumber, setRegisterationNumber] = useState('');
    const [studentData, setStudentData] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.get(`http://127.0.0.1:8000/students/${RegisterationNumber}`);
            setStudentData(response.data);
            setError(null);
        } catch (error) {
            setError(error.message);
            console.error('Error fetching student data:', error);
        }
    };

    const handleHostelUpdate = async (newHostelStatus) => {
    try {
      const response = await axios.put(
        `http://127.0.0.1:8000/students/${RegisterationNumber}/`,
        { insidehostel: newHostelStatus }
      );
      console.log('Hostel status updated:', response.data);
      setStudentData({RegisterationNumber: '225891256', FirstName: 'Kavin', insidehostel: newHostelStatus });
    } catch (error) {
      console.error('Error updating hostel status:', error);
    }
  };

    return (
        <div className="App">
            <img src={attendancepng}></img>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Registration Number"
                    id='inputstyle'
                    value={RegisterationNumber}
                    onChange={(e) => setRegisterationNumber(e.target.value)}
                />
                <div className='buttondiv'>
                    <button type="submit">Submit</button>
                </div>
            </form>
            <div className='admin'>
                <a href="http://127.0.0.1:8000/admin/">admin login</a>
            </div>
            {studentData && (
                <div>
                    <h2>Student Details</h2>
                    <p>Registration Number: {studentData.RegisterationNumber}</p>
                    <p>Name: {studentData.FirstName}</p>
                    <button onClick={() => handleHostelUpdate(true)}>In Hostel</button>
                    <button onClick={() => handleHostelUpdate(false)}>Out of Hostel</button>
                    <p>Current Hostel Status: {studentData.insidehostel ? 'In Hostel' : 'Out of Hostel'}</p>
                </div>
            )}
            {error && <p style={{color: 'red'}}>{error}</p>}

        </div>
    );
}

export default App;


/*export default Loginform*/
