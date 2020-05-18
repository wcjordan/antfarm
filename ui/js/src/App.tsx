import React from 'react';
// import Board from './components/tictactoe/Board'
import ControlPanel from './components/training/ControlPanel';
import DataStream from './components/training/DataStream';
import { startTraining } from './redux/reducers';
import { Episode, Step, TrainingRun } from './redux/types';
import { connect } from 'react-redux';
import './App.css';

export function App(props: Props) {
  const { startTraining, ...dataProps } = this.props;

  // <Board size={3} />
  return (
    <div className="App">
      <ControlPanel disabled={false} startTraining={startTraining} />
      <DataStream {...dataProps} />
    </div>
  );
}

type Props = {
  episodes: Episode[];
  startTraining: Function;
  steps: Step[];
  trainingRun: TrainingRun | null;
};

const mapStateToProps = (state: Props) => {
  return {
    episodes: state.episodes,
    steps: state.steps,
    trainingRun: state.trainingRun,
  };
};
const mapDispatchToProps = { startTraining };
export default connect(mapStateToProps, mapDispatchToProps)(App);
