import React from 'react';
import { connect } from 'react-redux';
import Board from './components/tictactoe/Board';
import ControlPanel from './components/training/ControlPanel';
import StatusBar from './components/training/StatusBar';
import { Episode, PlaybackEntry, ReduxState } from './redux/types';
import { startTraining } from './redux/reducers/trainingReducer';
import { togglePlayback } from './redux/reducers/playbackReducer';
import {
  selectSortedEpisodes,
  selectPlaybackEntry,
  selectPlaybackEpisode,
  selectWatchedSet,
} from './redux/selectors';
import './App.css';

export function App(props: Props) {
  const { playbackEntry, ...controlPanelProps } = props;
  const { board, moveInfo, iteration, reward } = playbackEntry;
  return (
    <div className="App">
      <ControlPanel {...controlPanelProps} />
      <div className="viewer">
        <StatusBar iteration={iteration} reward={reward} />
        <Board size={3} board={board} moveInfo={moveInfo} />
      </div>
    </div>
  );
}

type Props = {
  activeEpisode: number | null;
  episodes: Episode[];
  paused: boolean;
  playbackEntry: PlaybackEntry;
  startTraining: Function;
  togglePlayback: Function;
  watchedEpisodes: Set<number>;
};

const mapStateToProps = (state: ReduxState) => {
  const activeEpisode = selectPlaybackEpisode(state);
  return {
    activeEpisode: activeEpisode ? activeEpisode.id : null,
    episodes: selectSortedEpisodes(state),
    paused: state.playback.paused,
    playbackEntry: selectPlaybackEntry(state),
    watchedEpisodes: selectWatchedSet(state),
  };
};
const mapDispatchToProps = { startTraining, togglePlayback };
export default connect(mapStateToProps, mapDispatchToProps)(App);
