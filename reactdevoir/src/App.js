import logo from './logo.svg';
import './App.css';
import Calendrier from './composants/Calendrier'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1> Devoir reactjs </h1>
      </header>
      <main className="App-header">
        <Calendrier />
      </main>
    </div>
  );
}

export default App;
