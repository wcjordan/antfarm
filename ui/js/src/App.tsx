import React from 'react';
import { connect } from 'react-redux';
import './App.css';
import Board from './components/tictactoe/Board';
import ControlPanel from './components/training/ControlPanel';
// import DataStream from './components/training/DataStream';
import { PlaybackEntry, TrainingRun, ReduxState } from './redux/types';
import { startTraining } from './redux/reducers/trainingReducer';
import { selectPlaybackEntry } from './redux/selectors';

export function App(props: Props) {
  const { playbackEntry, startTraining } = props;
  const { board, moveInfo } = playbackEntry;
  return (
    <div className="App">
      <ControlPanel disabled={false} startTraining={startTraining} />
      <Board size={3} board={board} moveInfo={moveInfo} />
    </div>
  );
}

type Props = {
  playbackEntry: PlaybackEntry;
  startTraining: Function;
  trainingRun: TrainingRun | null;
};

const mapStateToProps = (state: ReduxState) => {
  return {
    playbackEntry: selectPlaybackEntry(state),
    trainingRun: state.training.trainingRun,
  };
};
const mapDispatchToProps = { startTraining };
export default connect(mapStateToProps, mapDispatchToProps)(App);
