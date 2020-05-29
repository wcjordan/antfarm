import React from 'react';
import StatusBar from './StatusBar';

export default {
  title: 'Status Bar',
  component: StatusBar,
};

const defaultProps = {
  iteration: 2,
  reward: -0.6,
};

export const DefaultView = () => <StatusBar {...defaultProps} />;
