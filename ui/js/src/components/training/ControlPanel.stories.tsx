import React from 'react';
import { action } from '@storybook/addon-actions';
import ControlPanel from './ControlPanel';

export default {
  title: 'Control Panel',
  component: ControlPanel,
};

const defaultProps = {
  activeEpisode: null,
  episodes: [],
  startTraining: action('start_training'),
  watchedEpisodes: new Set<number>(),
};

export const DefaultView = () => <ControlPanel {...defaultProps} />;
