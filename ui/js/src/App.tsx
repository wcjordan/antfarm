import React from 'react';
import { connect } from 'react-redux';
import './App.css';
import Board from './components/tictactoe/Board';
import ControlPanel from './components/training/ControlPanel';
// import DataStream from './components/training/DataStream';
import { Episode, Step, TrainingRun, ReduxState } from './redux/types';
import { startTraining } from './redux/reducers/trainingReducer';
import {
  selectEpisodes,
  selectOpponentMove,
  selectPlaybackStep,
  selectSteps,
} from './redux/selectors';

export function App(props: Props) {
  const { opponentMove, playbackStep, playerMoveStep, startTraining } = props;
  let playerMove = null;
  let boardState = null;
  if (playbackStep) {
    boardState = playbackStep.state;
    playerMove = playbackStep.action;
  }

  const moveInfo = {
    playerMove,
    opponentMove,
    playerMoveStep,
  };

  return (
    <div className="App">
      <ControlPanel disabled={false} startTraining={startTraining} />
      <Board size={3} boardState={boardState} moveInfo={moveInfo} />
    </div>
  );
}

type Props = {
  episodes: Episode[];
  opponentMove: string | null;
  playbackStep: Step | null;
  playerMoveStep: boolean;
  startTraining: Function;
  steps: Step[];
  trainingRun: TrainingRun | null;
};

const mapStateToProps = (state: ReduxState) => {
  return {
    episodes: selectEpisodes(state),
    opponentMove: selectOpponentMove(state),
    playbackStep: selectPlaybackStep(state),
    playerMoveStep: state.playback.playerMoveStep,
    steps: selectSteps(state),
    trainingRun: state.training.trainingRun,
  };
};
const mapDispatchToProps = { startTraining };
export default connect(mapStateToProps, mapDispatchToProps)(App);
