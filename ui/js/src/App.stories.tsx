import React from 'react';
import { App } from './App';
import { action } from '@storybook/addon-actions';

export default {
  title: 'App',
  component: App,
};

const defaultProps = {
  episodes: [],
  startTraining: action('start_training'),
  steps: [],
  trainingRun: null,
};
export const DefaultLayout = () => <App {...defaultProps} />;
