import React from 'react';
import { action } from '@storybook/addon-actions';
import { App } from './App';

export default {
  title: 'App',
  component: App,
};

const defaultProps = {
  playbackEntry: {
    board: null,
    moveInfo: {
      move: null,
      illegalMoves: [],
    },
  },
  startTraining: action('start_training'),
  trainingRun: null,
};
export const DefaultLayout = () => <App {...defaultProps} />;
