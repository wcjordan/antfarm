import _ from 'lodash';
import React from 'react';
import { action } from '@storybook/addon-actions';
import ControlPanel from './ControlPanel';

export default {
  title: 'Control Panel',
  component: ControlPanel,
};

const defaultProps = {
  activeEpisode: 112,
  episodes: _.times(15, idx => ({
    id: 100 + idx,
    iteration: idx,
    total_reward: Math.sin(idx),
    training_run: 1,
  })),
  paused: false,
  startTraining: action('start_training'),
  togglePlayback: action('toggle_playback'),
  watchedEpisodes: new Set<number>([112, 111, 113, 114]),
};

export const DefaultView = () => <ControlPanel {...defaultProps} />;
