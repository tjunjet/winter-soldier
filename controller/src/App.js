import './App.css';
import ReactPlayer from 'react-player';

function App() {
  return (
  <body>
    <div className="App">
        <img src="localhost:5412" width="720" height="480"/>
        <br></br>
        <br></br>
        <br></br>
        <table className="buttons">
          <tr>
            <td><button type="button" className="btn">INSERT JOYSTICK</button></td>
            <td><button type="button" className="btn">INSERT JOYSTICK</button></td>
          </tr>
        </table>
    </div>
  </body>
  );
}

export default App;
