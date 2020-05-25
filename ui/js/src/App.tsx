import React from 'react';
import { connect } from 'react-redux';
import './App.css';
import Board from './components/tictactoe/Board';
import ControlPanel from './components/training/ControlPanel';
// import DataStream from './components/training/DataStream';
import { Episode, PlaybackEntry, ReduxState } from './redux/types';
import { startTraining } from './redux/reducers/trainingReducer';
import {
  selectEpisodes,
  selectPlaybackEntry,
  selectPlaybackEpisode,
  selectWatchedSet,
} from './redux/selectors';

export function App(props: Props) {
  const { playbackEntry, ...controlPanelProps } = props;
  const { board, moveInfo } = playbackEntry;
  return (
    <div className="App">
      <ControlPanel {...controlPanelProps} />
      <Board size={3} board={board} moveInfo={moveInfo} />
    </div>
  );
}

type Props = {
  activeEpisode: number | null;
  episodes: Episode[];
  playbackEntry: PlaybackEntry;
  startTraining: Function;
  watchedEpisodes: Set<number>;
};

const mapStateToProps = (state: ReduxState) => {
  const activeEpisode = selectPlaybackEpisode(state);
  return {
    activeEpisode: activeEpisode ? activeEpisode.id : null,
    episodes: selectEpisodes(state),
    playbackEntry: selectPlaybackEntry(state),
    watchedEpisodes: selectWatchedSet(state),
  };
};
const mapDispatchToProps = { startTraining };
export default connect(mapStateToProps, mapDispatchToProps)(App);
