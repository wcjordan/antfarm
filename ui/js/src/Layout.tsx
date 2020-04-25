import React from 'react'
// import Board from './components/tictactoe/Board'
import ControlPanel from './components/training/ControlPanel'
import DataStream from './components/training/DataStream'
import './Layout.css'

function Layout(props: Props) {
  const { startTraining } = props

  // <Board size={3} />
  return (
    <div className="App">
      <ControlPanel disabled={false} startTrainingHandler={startTraining} />
      <DataStream />
    </div>
  )
}

type Props = {
  startTraining: Function
}

export default Layout
