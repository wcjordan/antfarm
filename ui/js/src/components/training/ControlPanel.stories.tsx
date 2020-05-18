import React from 'react';
import { action } from '@storybook/addon-actions';
import ControlPanel from './ControlPanel';

export default {
  title: 'Control Panel',
  component: ControlPanel,
};

export const DefaultView = () => (
  <ControlPanel disabled={false} startTraining={action('start_training')} />
);
