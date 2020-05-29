import React from 'react';
import './StatusBar.css';

function StatusBar(props: Props) {
  return (
    <div className="status-bar">
      <span className="step-iteration">Step: {props.iteration}</span>
      <span className="step-reward">Reward: {props.reward}</span>
    </div>
  );
}

type Props = {
  iteration: number;
  reward: number;
};

export default StatusBar;
