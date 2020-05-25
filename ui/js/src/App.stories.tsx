import React from 'react';
import { action } from '@storybook/addon-actions';
import { App } from './App';

export default {
  title: 'App',
  component: App,
};

const defaultProps = {
  activeEpisode: null,
  playbackEntry: {
    board: null,
    moveInfo: {
      move: null,
      illegalMoves: [],
    },
  },
  startTraining: action('start_training'),
  episodes: [],
  watchedEpisodes: new Set<number>(),
};
export const DefaultLayout = () => <App {...defaultProps} />;
