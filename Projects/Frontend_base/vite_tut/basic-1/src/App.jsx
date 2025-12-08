import { useState } from 'react'
import './App.css'
import RandomNumberGenerator from './components/random_number_genrator.jsx'

function App() {
  const [value, setValue] = useState(null);
console.log(value);



  const isEven = value !== null && value % 2 === 0;

  return (
    <div className="newspaper">
      <header className="masthead">
        <div className="edition">Vol. MMXXIV • No. {value || '—'}</div>
        <h1 className="title">THE SETH GAZETTE </h1>
        <div className="date">{new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}</div>
      </header>
      
      <div className="divider"></div>
      
      <main className="article">
        <h2 className="headline">Random Number Generator</h2>
        <div className={`result ${isEven ? 'even' : 'odd'}`}>
          <RandomNumberGenerator value={value} setValue={setValue} />
        </div>
      </main>
    </div>
  )
}

export default App
