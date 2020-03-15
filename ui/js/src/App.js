import Board from './components/tictactoe/Board.js'
import React from 'react'
import './App.css'

function App() {
  return (
    <div className="App">
      <Board size={3} />
    </div>
  )
}

export default App
