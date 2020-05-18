import React from 'react';
import ControlPanel from './ControlPanel';
import { action } from '@storybook/addon-actions';

export default {
  title: 'Control Panel',
  component: ControlPanel,
};

export const DefaultView = () => (
  <ControlPanel disabled={false} startTraining={action('start_training')} />
);
