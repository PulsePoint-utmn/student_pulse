import './App.css';

import Header from './Components/Header/Header';
import MainBlock from './Components/MainBlock/MainBlock';
import Navbar from './Components/Navbar/Navbar';

function App() {
  return (
    <div className="bg-black text-white">
      <Header/>
      <MainBlock/>
      {/* <Navbar/> */}
    </div>
  );
}

export default App;