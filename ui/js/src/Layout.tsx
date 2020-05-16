import React from 'react'
// import Board from './components/tictactoe/Board'
import ControlPanel from './components/training/ControlPanel'
import DataStream, {
  Episode,
  Step,
  TrainingRun,
} from './components/training/DataStream'
import './Layout.css'

function Layout(props: Props) {
  const { episodes, startTraining, steps, training_run } = props

  // <Board size={3} />
  return (
    <div className="App">
      <ControlPanel
        disabled={training_run !== null}
        startTrainingHandler={startTraining}
      />
      <DataStream
        trainingRun={training_run}
        episodes={episodes}
        steps={steps}
      />
    </div>
  )
}

type Props = {
  startTraining: Function
  episodes: Episode[]
  steps: Step[]
  training_run: TrainingRun | null
}

export default Layout
