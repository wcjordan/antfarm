import React from 'react';
import { action } from '@storybook/addon-actions';
import { App } from './App';

export default {
  title: 'App',
  component: App,
};

const defaultProps = {
  episodes: [],
  opponentMove: null,
  playbackStep: null,
  playerMoveStep: false,
  startTraining: action('start_training'),
  steps: [],
  trainingRun: null,
};
export const DefaultLayout = () => <App {...defaultProps} />;
