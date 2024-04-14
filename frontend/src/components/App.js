import './App.css';
import Loginform from './loginform';
import logo from '../images/mahe-bengaluru-logo.png'
function App() {
  return (
    <div className='maincontainer'>
    <div className='leftbox'>
      <img src={logo} className='image'/></div>
    <div className='rightbox'>
      <Loginform></Loginform>
    </div>
  
    </div>
  )
}

export default App;
