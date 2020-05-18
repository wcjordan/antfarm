import React, { Component, SyntheticEvent } from 'react';
import './ControlPanel.css';

class ControlPanel extends Component<Props> {
  static defaultProps = {
    disabled: false,
  };

  render() {
    return (
      <div className="control-panel">
        <div className="placeholder" />
        <div className="button start-button" onClick={this.startTraining}>
          Start Training
        </div>
      </div>
    );
  }

  startTraining = (event: SyntheticEvent<HTMLElement>) => {
    if (!this.props.disabled) {
      event.preventDefault();
      this.props.startTraining();
    }
  };
}

type Props = {
  disabled: boolean;
  startTraining: Function;
};

export default ControlPanel;
