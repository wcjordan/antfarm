import _ from 'lodash';
import React from 'react';
import { action } from '@storybook/addon-actions';
import { App } from './App';

export default {
  title: 'App',
  component: App,
};

const defaultProps = {
  activeEpisode: null,
  paused: false,
  playbackEntry: {
    board: null,
    moveInfo: {
      move: null,
      illegalMoves: _.times(40, () => [0, 0]),
    },
  },
  startTraining: action('start_training'),
  togglePlayback: action('toggle_playback'),
  episodes: [],
  watchedEpisodes: new Set<number>(),
};
export const DefaultLayout = () => <App {...defaultProps} />;
